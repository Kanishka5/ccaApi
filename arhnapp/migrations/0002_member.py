# Generated by Django 2.1.5 on 2019-01-19 06:15

import arhnapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhnapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('post', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=arhnapp.models.member_image_path)),
            ],
            options={
                'verbose_name_plural': 'Members',
            },
        ),
    ]