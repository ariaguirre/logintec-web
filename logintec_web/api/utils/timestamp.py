import socket
import binascii
from datetime import datetime

# def send_and_receive(s, message):
#     s.send(message.encode())
#     data = s.recv(1000)
#     return data

# def main():
#     HOST = "10.1.100.105"  
#     PORT = 2112  
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((HOST, PORT))
#         print("Connected")

#         message = '\x02sMN SetAccessMode 03 F4724744\x03'
#         print(message)
#         data = send_and_receive(s, message)
#         print(data)

#         now = datetime.now()
#         fecha_actual = f'\x02sMN LSPsetdatetime +{now.year} +{now.month} +{now.day} +{now.hour} +{now.minute} +{now.second} +{now.microsecond}\x03'
#         print(fecha_actual)
#         data_receive = send_and_receive(s, fecha_actual)
#         print(data_receive)    

#         message = '\x02sRN STlms\x03'
#         print(message.encode())
#         print(binascii.hexlify(message.encode()).decode("utf-8"))
#         data = send_and_receive(s, message)
#         print(data)
#         print(binascii.hexlify(data).decode("utf-8"))

#     except Exception as error:
#         print("rrorrror:", error)

#     finally:
#         s.close()

# if __name__ == "__main__":
#     main()


HOST = "10.1.100.105"  
PORT = 2112  

now = datetime.now()

año=now.year
mes=now.month
dia=now.day
hora=now.hour
minuto=now.minute
segundo=now.second
microseg=now.microsecond
print(now)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected")

message = '\x02sMN SetAccessMode 03 F4724744\x03'
print(message)
s.send(message.encode())
print("mensaje enviado")
data = s.recv(23)
print(data)

fechaactual='\x02sMN LSPsetdatetime +{} +{} +{} +{} +{} +{} +{}\x03'.format(año, mes, dia, hora, minuto, segundo, microseg)
s.send(fechaactual.encode())
print(fechaactual)
datarecive = s.recv(1000)
print(datarecive)

message = '\x02sRN STlms\x03'   #Verificar fecha
print(message.encode())
print(binascii.hexlify(message.encode()))
s.send(message.encode())
print("mensaje enviado")

data = s.recv(50)
print(data)
print(binascii.hexlify(data).decode("utf-8"))
print(binascii.hexlify(data))

s.close()
