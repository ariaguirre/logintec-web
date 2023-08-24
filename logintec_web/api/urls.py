from django.urls import path
from django.http import HttpResponse, JsonResponse
from .views import connect, stand_by, start_measure, stop_measure

urlpatterns = [
    path('', connect),
    path('standby/', stand_by),
    path('start/', start_measure),
    path('stop/', stop_measure),
]
