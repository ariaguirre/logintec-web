import socket, time, datetime, math, mysql.connector, random, binascii, re
from math import *
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import threading

def ancho(grados, diagonal, distY):
    return round(((math.sin(math.radians(grados))*diagonal)-distY), 2)

def alto(grados, diagonal, distZ):
    return round((distZ-(math.cos(math.radians(grados))*diagonal)),2)

def get_scandata():
    host = '10.1.100.105'
    port = 2112
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    acc = b'\x02sMN SetAccessMode 03 F4724744\x03'
    message = '\x02sRN LMDscandata\x03'
    s.send(message.encode())
    print('Mensaje enviado')
    rawData = s.recv(2000).decode()
    # print('RAWDATA', rawData)
    words = rawData.split()
    angulo_inicial = words[23]
    factor = words[21]
    print('factor', factor)
    data = ' '.join(words[25:])
    group = re.findall(r'[0-9A-Za-z]{2,3}', data)
    group.append(angulo_inicial)
    group.append(factor)
    valores = group
    result = ' '.join(valores)

    return result

def get_data(sensorHeight):  
    sensorHeight = float(sensorHeight)   
    data = get_scandata()
    # print('SCANDATA', data)
    words = data.split()
    angulo_inicial = ((int(words[-2], 16))/10000)
    factor = words[-1]
    mediciones = words[1:-2]
    print('angulo_inicial', angulo_inicial)
    decimal = []
    group = ''

    for char in mediciones:
        if char != ' ':
            group += char
            if factor[0] == '4':
                decimal.append((int(group, 16))*2)
                group = ''
            if factor[0] == '3':
                decimal.append(int(group, 16))
                group = ''
    print('decimal', decimal)
    decimal = [dec for dec in decimal if dec < 1458]  # /2 --> 729
    decimal_str = [str(dec) for dec in decimal]
    puntos = len(decimal_str)
    print('puntos: ', puntos)
    result = ' '.join(decimal_str)
    dist_objeto=270
    h_sensor= sensorHeight 
    print('sensorHeight', sensorHeight)
    salto=1/2
    values = [int(num) for num in result.split()]
    lista = []
    minYtotal = float('inf')
    maxZtotal = float('-inf')  #Chequear, sin valor negativo

    for a in range(1):
        x = (a+1)
        time.sleep(1) # un retraso de 1 segundo entre cada iteración del bucle
        minY = float('inf')
        maxZ = float('-inf')

        for b in range(0, puntos): 
            long_laser = round(values[b])
            alfa = round((angulo_inicial+(salto*b)), 2)
            # values[a][b] = long_laser
            y1 = ancho(alfa, long_laser, dist_objeto)
            z1 = alto(alfa, long_laser, h_sensor)
            minY = min(minY, y1)
            maxZ = max(maxZ, z1)
            lista.append([x, b+1, long_laser, alfa, y1, z1])
            # print('lista:', lista)
    lista1 = [item for item in lista if item[4] <= 900]
    lista2 = [item for item in lista1 if item[5] >= 8]
    minYtotal = min(minYtotal, minY)
    maxZtotal = max(maxZtotal, maxZ)
    medicionesx = int(len(lista1))
    print('medicionesx', medicionesx)
    print('minYtotal', minYtotal)
    print('maxZtotal', maxZtotal)

    return lista2


def plot_graph(allZ, allY):
    # plt.boxplot(allY, allZ, vert=False)
    plt.title('Grafico de datos')
    plt.plot(allY, allZ)
    plt.savefig('C:/Users/Depo01/Pictures/Graphs')
    plt.show()
    plt.close()
    return 'C:/Users/Depo01/Pictures/Graphs'

def clean_data():
    data = get_data()
    # print('dataaa', data)
    num = int(len(data))
    print('NUMMM', num)
    cleaned = []

    for sublist in data:
        negative = False
        for item in sublist:
            if item < 0:
                negative = True
                break
        if not negative:
            cleaned.append(sublist) #Elimina valores negativos

    # print("cleaned", cleaned)
    allY = []
    allZ = []
    for item in cleaned:
        allY.append(item[4])
        allZ.append(item[5])
    # allY, allZ
    print('allY', allY)
    print('allZ', allZ)

    graph_thread = threading.Thread(target=plot_graph, args=(allZ, allY))
    graph_thread.start()
    mediciones = int(len(cleaned))
    print("Mediciones:", mediciones)
    return cleaned


def get_output():
    host = '10.1.100.105'
    port = 2112
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = '\x02sRN LMPoutputRange\x03'
    # print(message.encode())
    # print(binascii.hexlify(message.encode()))
    s.send(message.encode())
    data = s.recv(50)
    print(data)
    print(binascii.hexlify(data).decode("utf-8"))
    print(binascii.hexlify(data))
    s.close()
    return data

def scanConfig():
    host = '10.1.100.105'
    port = 2112
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = '\x02sRN LMPscancfg\x03'
    s.send(message.encode())
    data = s.recv(50)
    print(data)
    print(binascii.hexlify(data).decode("utf-8"))
    print(binascii.hexlify(data))
    s.close()
    return data
    

if __name__ == '__main__':
    get_scandata()
    

