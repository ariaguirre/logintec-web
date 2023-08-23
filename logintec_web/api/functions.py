import socket
import binascii
from datetime import datetime

def get_connection(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("Conectado desde django")
        message = b'\x02sMN SetAccessMode 03 F4724744\x03'
        print(message)
        s.send(message)
        print("Mensaje enviado")
        data = s.recv(23)
        print("Response:", data)
        s.close()
        return data
    except Exception as e:
        print("Error:", e)
        return b""


def set_timestamp():
    get_connection()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    now = datetime.now()
    año=now.year
    mes=now.month
    dia=now.day
    hora=now.hour
    minuto=now.minute
    segundo=now.second
    microseg=now.microsecond
    print(now)

    fechaactual='\x02sMN LSPsetdatetime +{} +{} +{} +{} +{} +{} +{}\x03'.format(año, mes, dia, hora, minuto, segundo, microseg)
    s.send(fechaactual.encode())
    print(fechaactual)
    datarecive = s.recv(1000)
    print(datarecive)


def get_status():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = '\x02sRN STlms\x03'   #status stand_by
    print("Connected from django tested")
    print(message.encode())
    print(binascii.hexlify(message.encode()))
    s.send(message.encode())
    print("mensaje enviado")

    data = s.recv(50)
    print(data)
    print(binascii.hexlify(data).decode("utf-8"))
    print(binascii.hexlify(data))

def close():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()

if __name__ == '__main__':
    get_connection()