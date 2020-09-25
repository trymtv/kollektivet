# Generated by Django 3.0.5 on 2020-04-13 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klesvask', '0003_vask_vasker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('washType', models.CharField(max_length=100)),
                ('degrees', models.IntegerField()),
                ('washLength', models.IntegerField()),
                ('startTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('endTime', models.DateTimeField(null=True)),
                ('ongoing', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='vask',
        ),
    ]