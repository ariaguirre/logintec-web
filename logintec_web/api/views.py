from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .functions import get_connection, get_status, start, stop
from .scanFunctions import get_scandata, get_data
import binascii

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
    puntos = 205
    data = get_scandata(puntos)
    response = "\n".join(data) #Une los elementos de la lista con saltos de linea
    return HttpResponse(response)


def analyze_data(request):
    puntos = 205
    angulo_inicial = 17
    salto = 1/3
    angulo_final = 85
    distancia = 270
    h_sensor=820
    get_data(puntos, angulo_inicial, angulo_final, salto, distancia, h_sensor)
    return JsonResponse({'message': 'Datos analizados y guardados correctamente.'})