# Generated by Django 3.0.5 on 2020-04-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klesvask', '0007_washqueue_regdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='washqueue',
            name='washType',
            field=models.CharField(default='hvitvask', max_length=100),
            preserve_default=False,
        ),
    ]
