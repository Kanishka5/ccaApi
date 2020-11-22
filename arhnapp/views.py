from django.shortcuts import render
from .models import aarohanparticipant, Events, Feedback, Member, User, Slideshow, FlappyBird, PlayZone
from django.views import generic
from django.shortcuts import render, get_object_or_404, render
from .forms import arhnregform  # workshopregForm
from django.shortcuts import redirect
from django.core.mail import send_mail
from arhn import settings as sett
from .models import Events
from rest_framework import viewsets, status
from .serializers import EventSerializer, FeedSerializer, MemberSerializer, UserSerializer, SlideSerializer, FlappyBirdSerializer, PlayzoneSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
import xlwt


# landing page
def cca(request):
    return HttpResponse("CCA 2021 API")


# like an event
def like(request, string):
    try:
        event = Events.objects.get(title=str(string))
    except:
        return HttpResponse("not allowed")
    event.like_count += 1
    event.save()
    return HttpResponse(str(event.like_count))


# unlike an already liked event
def dlike(request, string):
    try:
        event = Events.objects.get(title=str(string))
    except:
        return HttpResponse("not allowed")
    if event.like_count < 1:
        return HttpResponse("not allowed")
    event.like_count -= 1
    event.save()
    return HttpResponse(str(event.like_count))


# get alll events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('-Date')
    serializer_class = EventSerializer


# get all user feedbacks
class FeedViewSet(viewsets.ModelViewSet):
    serializer_class = FeedSerializer
    queryset = Feedback.objects.all()


# all members of CCA
class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'cell']

# user adds feedback for a particular event
def feed(request, string):
    if string[1] == "-":
        r = string[0]
        c = string[2:]
        timenow = datetime.now()
        f = Feedback(rating=r, comment=c, Date=timenow)
        f.save()
        return HttpResponse("success")
    else:
        return HttpResponse("error")


# CCA user informations
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='get_email/(?P<email>\w[\w\.-]*@\w[\w\.-]+\.\w+)')
    def getByEmail(self, request, email):
        email = get_object_or_404(User, email=email)
        return Response(UserSerializer(email).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='edit_email/(?P<email>\w[\w\.-]*@\w[\w\.-]+\.\w+)')
    def EditByEmail(self, request, email, format=None):
        user = get_object_or_404(User, email=email)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# slideshow items
class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slideshow.objects.all()
    serializer_class = SlideSerializer


# flappyvhi user data
class FlappyViewSet(viewsets.ModelViewSet):
    queryset = FlappyBird.objects.all()
    serializer_class = FlappyBirdSerializer

    @action(detail=False, methods=['get'], url_path='get_email/(?P<email>\w[\w\.-]*@\w[\w\.-]+\.\w+)')
    def getByEmail(self, request, email):
        email = get_object_or_404(FlappyBird, email=email)
        return Response(FlappyBirdSerializer(email).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='edit_email/(?P<email>\w[\w\.-]*@\w[\w\.-]+\.\w+)')
    def EditByEmail(self, request, email, format=None):
        user = get_object_or_404(FlappyBird, email=email)
        serializer = FlappyBirdSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# export aarohan user data to excel sheet
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Aarohan participant')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['participant', 'college', 'mobile', 'email', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = aarohanparticipant.objects.all().values_list(
        'participant', 'college', 'mobile', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# all items in playzone
class PlayzoneViewSet(viewsets.ModelViewSet):
    queryset = PlayZone.objects.all()
    serializer_class = PlayzoneSerializer
