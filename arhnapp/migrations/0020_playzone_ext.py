# Generated by Django 2.1.5 on 2019-12-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhnapp', '0019_playzone_authreq'),
    ]

    operations = [
        migrations.AddField(
            model_name='playzone',
            name='ext',
            field=models.BooleanField(default=False),
        ),
    ]
