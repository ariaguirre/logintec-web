from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .functions import get_connection, get_status, start, stop
from .scanFunctions import get_scandata, scanConfig, get_output, get_data, clean_data
import binascii
import numpy as np
import matplotlib.pyplot as plt

# & c:/Users/Depo01/Desktop/logintec-web/logintec_web/venv/Scripts/Activate.ps1

def connect(request):
    response = get_connection()
    print("Response:", response)
    print("Hex Response:", binascii.hexlify(response).decode("utf-8"))

    if b'SetAccessMode 1' in response:
        return JsonResponse({'message': 'Conectado.'})
    else:
        return JsonResponse({'message': 'Error en la conexión.'})


def stand_by(request):
    data = get_status().decode("utf-8")  
    print('DATA DE STANDBY', data)
    
    parts = data.split() 
    date_part = parts[7] 
    time_part = parts[5]  
    
    response = f" {data} <br/> Hora: {time_part} - Fecha: {date_part}"
    return HttpResponse(response)  


def start_measure(request):
    data = start()
    print('data', data)
    print("Hex Response:", binascii.hexlify(data).decode("utf-8"))

    if b'LMCstartmeas 0' in data:
        return JsonResponse({'message': 'Iniciando medicion.'})
    else:
        return JsonResponse({'message': 'Error en el inicio de medicion.'})


def stop_measure(request):
    data = stop()
    return HttpResponse(data)


# Data views

def scandata(request):
    # puntos = 205
    data = get_scandata()
    return HttpResponse(data)


def list(request):
    sensorHeight = request.GET.get('height', 850) #default value
    data = get_data(sensorHeight)
    return HttpResponse(data)

def clean(request):
    sensorHeight = request.GET.get('height', 850) #default value
    data = clean_data(sensorHeight)
    return HttpResponse(data)


def scan_config(request):
    data = scanConfig()
    return HttpResponse(data)


def output(request):
    data= get_output()
    return HttpResponse(data)