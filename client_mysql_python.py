import socket

import pickle
HOST = 'localhost'
PORT = 50010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
def list_to_bytes(data):
    """
    metodo per trasformare le liste in bytes prima di inviarle con l'utilizzo del metodo send
    della libreria socket
    """
    if not isinstance(data, list):
        raise Exception("devi passare una lista alla funzione list_to_bytes")
    list_converted = pickle.dumps(data)
    return list_converted
while True:
    flag=True
    lista=[]
    data = s.recv(1024)
    if not data:
        break

    print('Received:', data.decode())
    
    
    user_input = input("Inserisci i dati richiesti : ")
   
    s.send(user_input.encode())
    if(user_input=="1",user_input=="2",user_input=="3",user_input=="4"):
        flag=False
    if(flag==False):
        data = s.recv(1024)
        if not data:
            break

        print('Received:', data.decode())


        user_input = input("Inserisci i dati richiesti : ")
        lista.append(user_input)
        list_to_bytes(lista)

        s.send(lista)
        lista.clear()
        

   



s.close()
