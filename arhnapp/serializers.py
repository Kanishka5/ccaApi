from .models import Events,Feedback,Member,User,Slideshow,FlappyBird,PlayZone
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('title', 'location', 'description', 'details', 'image','Date','like_count','event_link', 'event_link_name','order')


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('rating', 'comment','event')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'year','post','cell','image','order')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'string')

class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slideshow
        fields = ('image','slide_link','order')

class FlappyBirdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlappyBird
        fields = ('name','email','score')

class PlayzoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayZone
        fields = ('name','image','order','link','authreq','ext')
