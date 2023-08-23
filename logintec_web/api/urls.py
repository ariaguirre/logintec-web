from django.urls import path
from django.http import HttpResponse, JsonResponse
from .views import main
from .views import connect
from .import views
from .functions import get_connection

urlpatterns = [
    path('', connect),
]

# def connect(request):
#     host = request.GET.get('host')
#     port = int(request.GET.get('port'))
#     result = get_connection(host, port)
    
#     return JsonResponse({'message': result})