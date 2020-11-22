from django.db import models
import os

class aarohanparticipant(models.Model):
    participant=models.CharField(max_length=300,blank=False)
    college=models.CharField(max_length=50,blank=False)
    mobile=models.CharField(max_length=10,blank=False)
    email=models.EmailField(max_length=50,blank=False)
    def publish(self):
        self.save()
    def __str__(self):
        return self.participant
    class Meta:
        verbose_name_plural = "Aarohan_Participants"

def image_path(instance_id,filename):
        return os.path.join('photos',str(instance_id),filename)

class Events(models.Model):
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    details = models.TextField()
    image = models.ImageField(upload_to=image_path)
    Date = models.DateTimeField(auto_now_add=False)
    like_count = models.IntegerField(default=0)
    description = models.TextField(max_length=2000)
    event_link = models.CharField(max_length=70)
    event_link_name = models.CharField(max_length=45)
    order = models.IntegerField()
    class Meta:
        verbose_name_plural = "Events"
    def str(self):
        return self.title


class Feedback(models.Model):
    rating=models.IntegerField(default=5,)
    comment=models.TextField(max_length=200)
    event = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Feedback"
    def str(self):
        return self.rating

def member_image_path(instance_id,filename):
        return os.path.join('members',str(instance_id),filename)


CELL_CHOICES = (
    ('core','CORE'),
    ('wdct', 'WDCT'),
    ('e-cell','E-CELL'),
    ('robo','ROBO'),
    ('r&d','R&D'),
    )



class Member(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    post = models.CharField(max_length=40)
    cell=models.CharField(choices=CELL_CHOICES,max_length=6)
    image = models.ImageField(upload_to=member_image_path)
    order = models.IntegerField()
    class Meta:
        verbose_name_plural = "Members"
    def str(self):
        return self.name

class User(models.Model):
    email = models.EmailField(primary_key=True,max_length=30)
    string = models.CharField(max_length=1000,blank=True)
    class Meta:
        verbose_name_plural = "User"
    def str(self):
        return self.email

def slide_image_path(instance_id,filename):
        return os.path.join('slideshow',str(instance_id),filename)

class Slideshow(models.Model):
    image = models.ImageField(upload_to=slide_image_path)
    slide_link = models.CharField(max_length=120)
    order = models.IntegerField()
    class Meta:
        verbose_name_plural = "Slideshow"
    def str(self):
        return self.slide_link

class FlappyBird(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True,max_length=30)
    score = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "FlappyBird"
    def str(self):
        return self.name

def playzone_image_path(instance_id,filename):
        return os.path.join('playzone',str(instance_id),filename)

class PlayZone(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to=playzone_image_path)
    order = models.IntegerField()
    link = models.CharField(max_length=555)
    authreq = models.BooleanField(default=False)
    ext = models.BooleanField(default=False)
