
# # DOCUMENTACIÓN
# Establecimiento de conexión servidor/cliente
# ¬https://www.youtube.com/watch?v=-ve1ZtDrUCo
# Establecimiento de encriptacion DES
# ¬https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
#Codigo adaptado para las necesidades del problema
from Crypto.Cipher import DES
import socket
cont=1


def leer():
    archivo=open('mensajerecibido.txt','rb')
    a=archivo.read()
    archivo.close()
    return a

b=input('ingrese el la clave del servidor b que es privada : ')

socket_ser=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_ser.bind(('localhost',8585))
socket_ser.listen()
print('El server ta ready')
print('se iniciaran los protocolos de sincronizacion con el cliente, por favor sigua las intrucciones')
while True:
    socketconexion,add=socket_ser.accept()
    print('se conecto ', add)

    while True:
        mensaje_recibido=socketconexion.recv(1024).decode()
    
        if 'clave ' in mensaje_recibido:
            P=mensaje_recibido.strip('clave ')
            print('credenciales recividas')
            print('aprete enter')
            P=P.split(' ')
            A=int(P[1])
            G=int(P[2])
            P=int(P[0])
            print('---')
            B = str(pow(G,int(b),P))
            #print(B) 
        elif 'mandame B' in mensaje_recibido:
            socketconexion.send(('esta es B '+B).encode())
            print('B mandado, escriba "ok"')
            kb=str(pow(A,int(b),P))
        elif 'Esta es ka'in mensaje_recibido:
            ka=mensaje_recibido.strip('Esta es ka')
            ka=(ka)
            if ka==kb:
                print('Las credenciales son iguales, presione enter')
                print('ya pueden empezar a comunicarse')
            if ka!=kb:
                print('este es kb: ',kb)
                print('no lo son')
                socketconexion.close()
                break
        elif 'se ha mandado un mensaje codificado, revisa' in mensaje_recibido:
            mensaje=leer()
            key=B'12345678'
            des = DES.new(key, DES.MODE_ECB)
            mensaje=des.decrypt(mensaje)
            # des 1
            key=B'12345678'
            des1= DES.new(key, DES.MODE_ECB)
            mensaje2=des1.decrypt(mensaje)
            #des 2
            key=B'12345678'
            des2= DES.new(key, DES.MODE_ECB)
            mensaje3=des2.decrypt(mensaje2)
            #des 3
            key=B'12345678'
            des3= DES.new(key, DES.MODE_ECB)
            mensaje4=des3.decrypt(mensaje3)

            print('el mensaje es: ',mensaje4.decode())
    
        elif mensaje_recibido=='-cerrar-':
            break
        else:
            if 'Enviar texto codificado' in mensaje_recibido:
                print('')
            elif cont==1:
                print('ya esta listo, Escriba "se esta viendo"')
                cont+=1
            else:
                print('--->',mensaje_recibido)
        socketconexion.send(input().encode())
        
    print('se desconecto la conexion con: ',add)
    socketconexion.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
