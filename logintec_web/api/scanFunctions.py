import socket, time, datetime, math, mysql.connector, random
import binascii
from math import *
from datetime import datetime

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
    print('DATA:', rawData)
    # inicio = rawData.find("CD")+3

    # data = rawData[inicio:inicio+(puntos*4)].split()

    # valid_data = []
    # for value in data:
    #     try:
    #         int(value, 16) #intenta convertir el valor a hexa
    #         valid_data.append(value)
    #     except ValueError:
    #         pass

    return rawData



def get_data(puntos, angulo_inicial, angulo_final, salto, distancia, h_sensor):
    hexa = []
    deci = []
    barcode = random.randint(99999999, 1000000000)
    print(barcode)
    hora = datetime.now
    
    host = '10.1.100.105'
    port = 2112
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    
    f = open("prueba.txt", "w")

    a = 0
    hexa = get_scandata(puntos)
    x = a + 1
    time.sleep(1)
    print('HEXA: ', hexa)

    long_laser_values = []
    for b in range(0, puntos):
        long_laser = round(int(hexa[b], 16))
        long_laser_values.append(long_laser)  # Store the values in the new list
        print('long_laser', long_laser)
        print('long_laser_values', long_laser_values)
        alfa = round((angulo_inicial + (salto * b)), 2)
        y1 = ancho(alfa, long_laser, distancia)
        z1 = alto(alfa, long_laser, h_sensor)
        deci.append([x, b + 1, long_laser, alfa, y1, z1]) #long_laser primer vagon de 3. alfa es angulo que le corresponde a cada vagon (1ro 17, se van sumando de 0.1667)
        print('deci', deci)
        f.write(str(x) + "\t" + str(y1) + "\t" + str(z1) + "\t" + str(long_laser) + "\t" + str(alfa) + "\n")

    f.close()
    s.close()
    print("Conexion finalizada")     
    mediciones = int(len(hexa))
    print("Cantidad de mediciones: ", mediciones)

    minY = min(deci, key=lambda item:item[4]) #minY punto mas cerca del sensor horizontal
    maxZ = max(deci, key=lambda item:item[5]) #maxZ punto vertical mas alto
    print('minY: ', minY[4])
    print('maxZ: ', maxZ[5])
    print("HEXA: ", hexa)
    print("DECI: ", deci)

    f = open("data.txt", "a")
    f.write(str(barcode)+"\t"+str(x)+"\t"+str(minY[4])+"\t"+str(maxZ[5])+"\t"+str(hora)+"\n")
    f.close()


def output():
    host = '10.1.100.105'
    port = 2112
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = '\x02sRN LMPoutputRange\x03'
    print(message.encode())
    print(binascii.hexlify(message.encode()))
    s.send(message.encode())
    print("mensaje enviado")

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
    # print(message.encode())
    # print(binascii.hexlify(message.encode()))
    s.send(message.encode())
    data = s.recv(50)
    print(data)
    print(binascii.hexlify(data).decode("utf-8"))
    print(binascii.hexlify(data))
    s.close()
    return data

    


if __name__ == '__main__':
    get_scandata()
    get_data()
    


#MI FUNCION ANTES

# import socket, time, datetime, math, mysql.connector, random
# from math import *
# from datetime import datetime

# def ancho(grados, diagonal, distY):
#     return round(((math.sin(math.radians(grados))*diagonal)-distY), 2)

# def alto(grados, diagonal, distZ):
#     return round((distZ-(math.cos(math.radians(grados))*diagonal)),2)

# def get_scandata(puntos):
#     host = '10.1.100.105'
#     port = 2112
#     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host,port))
#     message = '\x02sRN LMDscandata\x03'
#     s.send(message.encode())
#     print('Mensaje enviado')
#     rawData = s.recv(1024).decode()
#     print('DATA:', rawData)
#     inicio = rawData.find("CD")+3
#     data = rawData[inicio:inicio+(puntos*4)].split()
#     s.close
#     return data

# barcode = random.randint(99999999, 1000000000)
# print(barcode)
# hexa = []
# deci = []
# puntos = 205
# angulo_inicial = 27
# salto = 1/3
# angulo_final = 85
# distancia = 270
# h_sensor=820
# hora = datetime.now


# def get_data():
#     for a in range(1):
#         hexa.append(get_scandata(puntos))
#         x  = (a+1)
#         time.sleep(1)
#         for b in range(0,205):
#             long_laser = round(int(hexa[a][b], 16)) #mediciones de hexa a decimal
#             alfa = round((angulo_inicial+(salto*b)), 2) #angulo actual de medicion
#             hexa[a][b] = (long_laser) #se le asigna a la posicion de la lista su ubicacion del largo del laser
#             y1 = ancho(alfa, long_laser, distancia) #calculo y
#             z1 = alto(alfa, long_laser, h_sensor) #calculo z
#             deci.append([x, b+1, long_laser, alfa, y1, z1]) #Genera lista

#             host = '10.1.100.105'
#             port = 2112
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.connect((host, port))
#             print("CONECTADO GET DATA")
#             f = open("prueba.txt", "w")
#             f.write(str(x)+"\t"+str(y1)+"\t"+str(z1)+"\t"+str(long_laser)+"\t"+str(alfa)+"\n")       
#             f.close()
#             s.close()
#             print("Conexion finalizada")     
#             mediciones = int(len(hexa))
#             print("Cantidad de mediciones: ", mediciones)

#             minY = min(deci, key=lambda item:item[4]) #minY
#             maxZ = max(deci, key=lambda item:item[5]) #maxZ
#             print('minY: ', minY[4])
#             print('maxZ: ', maxZ[5])
#             print("HEXA: ", hexa)
#             print("DECI: ", deci)

#             f = open("data.txt", "a")
#             f.write(str(barcode)+"\t"+str(x)+"\t"+str(minY[4])+"\t"+str(maxZ[5])+"\t"+str(hora)+"\n")
#             f.close()


# if __name__ == '__main__':
#     get_scandata()
#     get_data()
    