# Generated by Django 2.1.5 on 2019-12-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhnapp', '0018_playzone'),
    ]

    operations = [
        migrations.AddField(
            model_name='playzone',
            name='authreq',
            field=models.BooleanField(default=False),
        ),
    ]
