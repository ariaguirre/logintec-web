from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .functions import get_connection
import binascii

def main(request):
    return HttpResponse('<h1>Hola</h1>')


def connect(request):
    host = "10.1.100.105"
    port = 2112 
    response = get_connection(host, port)
    
    print("Response:", response)
    print("Hex Response:", binascii.hexlify(response).decode("utf-8"))

    if b'SetAccessMode 1' in response:
        return JsonResponse({'message': 'Conectado.'})
    else:
        return JsonResponse({'message': 'Error en la conexión.'})
