from klesvask.models import Wash, WashQueue
from django.utils import timezone
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
            try:
                if Wash.objects.last():
                    lastWash = Wash.objects.last()
                    if lastWash.ongoing:
                        if timezone.now() > lastWash.endTime:
                            lastWash.ongoing = False
                            lastWash.save(update_fields=['ongoing'])
                            if lastWash.user.email:
                                send_mail(
                                    'Vasken er Ferdig',
                                    'Din ' + lastWash.washType + ' på ' + str(lastWash.degrees) + ' grader er ferdig!',
                                    'kollektivetmelding@gmail.com',
                                    [lastWash.user.email],
                                    fail_silently=False,
                                )
                            if WashQueue.objects.first():
                                queueUser = WashQueue.objects.first().user
                                if queueUser.email:
                                            send_mail(
                                                'Vaskemaskinen er ledig',
                                                lastWash.user.username + ' er ferdig med å vaske!',
                                                'kollektivetmelding@gmail.com',
                                                [queueUser.email],
                                                fail_silently=False,
                                            )
                                WashQueue.objects.filter(user=queueUser).delete()

            except:
                print("Error updating ongoing washes.")