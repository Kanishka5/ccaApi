# Generated by Django 2.1.5 on 2019-02-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhnapp', '0014_flappybird'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]