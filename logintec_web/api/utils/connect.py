import socket   
import binascii

def Main():
    host = '10.1.100.105'
    port = 2112

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Conectado al sensor")

    message = '\x02sMN SetAccessMode 03 F4724744\x03'
    s.send(message.encode)
    print("Mensaje enviado")

    data = s.recv(23)
    print(data)
    print(binascii.hexlify(data).decode("utf-8"))
    print(binascii.hexlify(data))

if __name__ == '__main__':
    Main()