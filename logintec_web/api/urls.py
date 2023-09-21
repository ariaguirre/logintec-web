from django.urls import path
from django.http import HttpResponse, JsonResponse
from .views import connect, stand_by, start_measure, stop_measure, scandata, scan_config, output, list, clean

urlpatterns = [
    path('connect/', connect),
    path('standby/', stand_by),
    path('start/', start_measure),
    path('stop/', stop_measure),
    path('scandata/', scandata),
    path('config/', scan_config),
    path('output/', output),
    path('list/', list),
    path('clean/', clean),
]
