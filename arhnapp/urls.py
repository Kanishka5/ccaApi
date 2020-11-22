from django.urls import path
from django.conf.urls import url,include
from arhnapp import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from rest_framework import routers
from arhnapp import views

# rest api endpoints
router = routers.DefaultRouter()
router.register('events', views.EventViewSet)
router.register('feedback', views.FeedViewSet)
router.register('members', views.MemberViewSet,basename="member")
router.register('users', views.UserViewSet)
router.register('slideshow', views.SlideViewSet)
router.register('flappybird', views.FlappyViewSet)
router.register('playzone', views.PlayzoneViewSet)


# all urls
urlpatterns = [
    url('api/like/(?P<string>[a-zA-Z_ ]+)/$',views.like,name="like"),
    url('api/dlike/(?P<string>[a-zA-Z_ ]+)/$',views.dlike,name="dlike"),
    url('feed/(?P<string>.+)/$',views.feed,name="feed"),
    url('api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.cca,name=''),
    # url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
