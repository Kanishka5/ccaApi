# Generated by Django 2.1.5 on 2019-01-19 00:07

import arhnapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aarohanparticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.CharField(max_length=300)),
                ('college', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Aarohan_Participants',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to=arhnapp.models.image_path)),
                ('Date', models.DateTimeField()),
                ('like_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5)),
                ('comment', models.TextField(max_length=200)),
                ('Date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
