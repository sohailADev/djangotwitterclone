# Generated by Django 3.1 on 2020-09-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_flag',
            field=models.BooleanField(default=False),
        ),
    ]
