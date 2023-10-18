import socket, time, datetime, math, mysql.connector, random, binascii, re
from math import *
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import threading

# FUNCIONES DE MANEJO DEL SCANNER

def ancho(grados, diagonal, distY):
    return round(((math.sin(math.radians(grados))*diagonal)-distY), 2)

def alto(grados, diagonal, distZ):
    return round((distZ-(math.cos(math.radians(grados))*diagonal)),2)

def get_scandata(): #Funcion para traer la informacion leida por el escaner
    host = '10.1.100.105'
    port = 2112
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))  # Conexion via socket con el scanner
    acc = b'\x02sMN SetAccessMode 03 F4724744\x03'      
    message = '\x02sRN LMDscandata\x03'     #Mensaje para pedirle la informacion leida
    s.send(message.encode())
    print('Mensaje enviado')
    rawData = s.recv(2000).decode()     #Recibo la informacion del scaner "raw"
    words = rawData.split()
    angulo_inicial = words[23]      #Obtengo el angulo inicial de medicion
    factor = words[21]      #Obtengo el factor de medicion 
    print('factor', factor)
    data = ' '.join(words[25:])     #Agrupo todas las medidas obtenidas
    group = re.findall(r'[0-9A-Za-z]{2,3}', data)       #vienen en valores de 2 o 3 caracteres
    group.append(angulo_inicial)        #agrego el angulo inicial y el factor de medicion al grupo de medidas
    group.append(factor)
    valores = group
    result = ' '.join(valores)

    return result     

def get_data(sensorHeight):     #Funcion para trabajar las medidas obtenidas
    sensorHeightF = int(float(sensorHeight))        #Recibo la altura del sensor traida desde el frontend ("Home.jsx")
    data = get_scandata()       #traigo la informacion recibida del sensor en hexadecimal
    words = data.split()
    angulo_inicial = ((int(words[-2], 16))/10000)   #Convierto el angulo inicial en decimal
    factor = words[-1]      #identifico el factor y las medidas
    mediciones = words[1:-2]
    print('angulo_inicial', angulo_inicial)
    decimal = []
    group = ''

    for char in mediciones:
        if char != ' ':
            group += char
            if factor[0] == '4':    
                decimal.append((int(group, 16))*2)  #Si el scale factor inicia con 4 (osea es 40000000h), multiplico todas las medidas decimales x 2
                group = ''
            if factor[0] == '3':
                decimal.append(int(group, 16)) #Si no inicia con 4 (osea es 3F800000h), no lo modifico
                group = ''
    decimal = [dec for dec in decimal if dec < 1458]  # Elimino todas las medidas superiores a 1458 (5B2)
    decimal_str = [str(dec) for dec in decimal] 
    puntos = len(decimal_str)       #Cantidad de puntos medidos
    print('puntos: ', puntos)
    result = ' '.join(decimal_str)
    dist_objeto=270
    h_sensor= sensorHeightF or 840 # En caso de no recibir altura del sensor, este es el valor por default
    print('SENSOR HEIGHT', sensorHeightF)
    salto=1/2       #Salto de medida del sensor
    values = [int(num) for num in result.split()]
    lista = []
    minYtotal = float('inf')    #Establece el valor minimo total de Y
    maxZtotal = float('-inf')   #Establece el valor maximo total de X

    for a in range(1):  #Establece bucle que se ejecutara una vez
        x = (a+1)  #Recuento de iteraciones
        time.sleep(1) # un retraso de 1 segundo entre cada iteración del bucle
        minY = float('inf') #inicializan las variables minY y maxZ con valores extremos. minY se inicializa con infinito positivo y maxZ con infinito negativo
        maxZ = float('-inf')    # para que puedan ser actualizadas con valores reales más adelante

        for b in range(0, puntos):  #Bucle para ejecutar por la cantidad de puntos medidos
            long_laser = round(values[b])
            alfa = round((angulo_inicial+(salto*b)), 2)
            # values[a][b] = long_laser
            y1 = ancho(alfa, long_laser, dist_objeto)       #utilizo las funciones declaradas al inicio
            z1 = alto(alfa, long_laser, h_sensor)
            minY = min(minY, y1)    #actualiza las variables declaradas a sus valores reales
            maxZ = max(maxZ, z1)
            lista.append([x, b+1, long_laser, alfa, y1, z1])
    lista1 = [item for item in lista if item[4] <= 900 and item[4] > 2]  #Elimino los valores de Y que sean mayores a 900 y menores a 2
    lista2 = [item for item in lista1 if item[5] >= 10.5]  #Elimino los valores de Z que sean menores a 10.5
    minYtotal = min(minYtotal, minY)
    maxZtotal = max(maxZtotal, maxZ)
    medicionesx = int(len(lista1))
    print('medicionesx', medicionesx)
    print('minYtotal', minYtotal)
    print('maxZtotal', maxZtotal)

    return lista2


def plot_graph(allZ, allY):     #Funcion para graficar los datos convertidos
    plt.figure()
    plt.title('Grafico de datos')
    plt.plot(allY, allZ)    #Datos a pasar
    plt.grid()
    plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])  #Valores de eje X
    plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450])     #Valores de Y
    plt.savefig('C:/Users/Depo01/Pictures/Graphs')
    plt.show()
    plt.close()
    return 'C:/Users/Depo01/Pictures/Graphs'

def clean_data(sensorHeight):   #Funcion para limpiar la data del sensor
    data = get_data(sensorHeight)
    num = int(len(data))
    cleaned = []

    for sublist in data:    #bucle para eliminar valores negativos leidos en el sensor (fuera de alcance)
        negative = False
        for item in sublist:
            if item < 0:
                negative = True
                break
        if not negative:
            cleaned.append(sublist) #Elimina valores negativos

    allY = []
    allZ = []
    for item in cleaned:
        allY.append(item[4])
        allZ.append(item[5])

    graph_thread = threading.Thread(target=plot_graph, args=(allZ, allY))      #llamo a plot_graph() para mostrar el grafico en pantalla
    graph_thread.start()
    mediciones = int(len(cleaned))
    print("Mediciones:", mediciones)
    return cleaned


def get_output():   #Funcion para configurar amplitud y resolucion angular 
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

def scanConfig():   #Funcion de ayuda para configurar encoder
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
    

