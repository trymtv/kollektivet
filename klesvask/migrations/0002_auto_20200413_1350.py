# Generated by Django 3.0.5 on 2020-04-13 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klesvask', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vask',
            old_name='type',
            new_name='vask_type',
        ),
    ]
