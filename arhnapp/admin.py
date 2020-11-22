from django.contrib import admin
from .models import aarohanparticipant,Events,Feedback,Member,User,Slideshow,FlappyBird,PlayZone
# Register your models here.

#admin.site.register(event1participants)

class AarohanAdmin(admin.ModelAdmin):
    list_display = ('participant','college','mobile','email')

admin.site.register(aarohanparticipant, AarohanAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','order','Date',)

admin.site.register(Events, EventAdmin)

admin.site.register(Feedback)
admin.site.register(User)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('slide_link','order')
admin.site.register(Slideshow, SlideAdmin)



#admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','post','cell','year',)

admin.site.register(Member, MemberAdmin)

class FlappyAdmin(admin.ModelAdmin):
    list_display = ('name','email','score')

admin.site.register(FlappyBird, FlappyAdmin,)

class PlayzoneAdmin(admin.ModelAdmin):
    list_display = ('name','image','order','link')

admin.site.register(PlayZone, PlayzoneAdmin)


