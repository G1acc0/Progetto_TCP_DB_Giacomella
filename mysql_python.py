import socket
import mysql.connector
import threading
import pickle
def bytes_to_list(data):
    """
    metodo per trasformare i bytes in liste una volta ricevute con l'utilizzo del metodo recv
    della libreria socket
    """
    if not isinstance(data, bytes):
        raise Exception("devi passare dei bytes alla funzione bytes_to_list")

    return pickle.loads(data)
#-----------------------------------------------------------------------------------
def db(cconn,i,risp):
    tabelle={'dipendenti':'dipendenti_marco_giacomella','zone':'zone_di_lavoro_marco_giacomella'}
    colonne=[]
    onn = mysql.connector.connect(
                    host="127.0.0.1", # 10.10.0.10  
                    user="root",#"marco_giacomella",
                    #password="giacomella1234",
                    database="5Btepsit",
                    port=3306, 
                    )
    cur = onn.cursor()
    print("sono qui")
    print(risp)
#---------------------------------------------------------------------------------------------------------------------------
    if (risp == "1"):
      print("sono nella funzione 1")
      cconn[i][0].send("Inserisci la tabella su cui vuoi inserire: ".encode())
      
      tabella_scelta = cconn[i][0].recv(1024).decode()

      if tabella_scelta in tabelle:
            tabella = tabelle[tabella_scelta]
            query_colonne = f"SHOW COLUMNS FROM {tabella}"

            try:
                cur.execute(query_colonne)
                colonne = [col[0] for col in cur.fetchall()]
                cconn[i][0].send(f"Le colonne da inserire sono queste: {colonne}\n".encode())
               
                risp3 = cconn[i][0].recv(1024)
                bytes_to_list(risp3)

                query_inserimento = f"INSERT INTO {tabella} VALUES ({', '.join(['%s' for _ in colonne])})"
                cur.execute(query_inserimento, tuple(risp3.split(',')))
                onn.commit()

                cconn[i][0].send("Inserimento riuscito\n".encode())
                
            except mysql.connector.Error as err:
                cconn[i][0].send(f"Errore durante l'inserimento: {err}\n".encode())
                
      else:
            cconn[i][0].send("Tabella non valida\n".encode())
            

#----------------------------------------------------------------------------------------------------------------------------------


    if (risp=="2"):
      print("sono nella funzione 2")
      cconn[i][0].send("Inserisci la tabella sul quale vuoi leggere".encode())
      
      risp2=cconn[i][0].recv(1024).decode()
      if(risp2 in tabelle.keys()):
          tabella=tabelle.get(risp2)
          query = f"SHOW COLUMNS FROM {tabella}"
          try:
            cur.execute(query)
          except Exception:
            cconn[i][0].send("Tabella non corretta - MYSQL Error".encode())
           
            cconn[i][0].close()
        

          dati = cur.fetchall()
          dati_attributi=[]
          for riga in dati:
            dati_attributi.append(riga[0])
          cconn[i][0].send(f"Le colonne che si possono leggere sono queste {dati_attributi} quali vuoi leggere\n".encode())
          
          colonne.append(bytes_to_list(cconn[i][0].recv(1024)))
          if(colonne in dati_attributi or colonne=='*'):
              if(colonne=='*'):
                  query=f"SELECT {colonne} FROM {tabella} "
                  cur.execute(query)
                  dati=cur.fetchall()
                  print(dati)
              else:
                cconn[i][0].send("Inserisci il valore che vuoi confermare nella tabella\n".encode())
                risp3=bytes_to_list(cconn[i][0].recv(1024))
              
                query=f"SELECT {colonne} FROM {tabella} where {colonne}={risp3}"
                cur.execute(query)
                
                dati=cur.fetchall()
                print(dati)
          elif(colonne not in dati_attributi ):
              cconn[i][0].send("L'attributo non esiste".encode())
              

          
      else:
             cconn[i][0].send("Inserimento errato riprovare".encode())
             

#----------------------------------------------------------------------------------------------------------------------------------



    if (risp=="3"):
      print("sono nella funzione tre")
      cconn[i][0].send("Inserisci la tabella sul quale vuoi eliminare".encode())
      
      risp2=cconn[i][0].recv(1024).decode()
      if(risp2 in tabelle.keys()):
          tabella=tabelle.get(risp2)
          query = f"SHOW COLUMNS FROM {tabella}"
          try:
            cur.execute(query)
          except Exception:
            cconn[i][0].send("Tabella non corretta - MYSQL Error".encode())
        

          dati = cur.fetchall()
          dati_attributi=[]
          for riga in dati:
            dati_attributi.append(riga[0])
          cconn[i][0].send(f"Le colonne dove si può eliminare sono queste {dati_attributi} quali vuoi modificare\n".encode())
          
          colonne.append(bytes_to_list(cconn[i][0].recv(1024)))
          if(colonne in dati_attributi ):
              
                cconn[i][0].send("Inserisci il valore che vuoi modificare nella tabella\n".encode())
                
                risp3=bytes_to_list(cconn[i][0].recv(1024))
                cconn[i][0].send("Inserisci il valore che vuoi inserire nella tabella\n".encode())
                
                risp4=bytes_to_list(cconn[i][0].recv(1024))
                query=f"UPDATE {tabella}  SET {risp4} where {colonne}={risp3}"
                cur.execute(query)
                cconn[i][0].send("Elementi aggiornati\n".encode())
                
          elif(colonne not in dati_attributi ):
              cconn[i][0].send("L'attributo non esiste".encode())
              
              cconn[i][0].close()

          
      else:
            cconn[i][0].send("Inserimento errato riprovare".encode())
            
            cconn[i][0].close()


#----------------------------------------------------------------------------------------------------------------------------------

    if (risp=="4"):
      print("sono nella funzione quattro")
      cconn[i][0].send("Inserisci la tabella sul quale vuoi eliminare".encode())
      
      risp2=cconn[i][0].recv(1024).decode()
      if(risp2 in tabelle.keys()):
          tabella=tabelle.get(risp2)
          query = f"SHOW COLUMNS FROM {tabella}"
          try:
            cur.execute(query)
          except Exception:
            cconn[i][0].send("Tabella non corretta - MYSQL Error".encode())
            
            cconn[i][0].close()
        

          dati = cur.fetchall()
          dati_attributi=[]
          for riga in dati:
            dati_attributi.append(riga[0])
          cconn[i][0].send(f"Le colonne dove si può eliminare sono queste {dati_attributi} quali vuoi eliminare\n".encode())
          
          colonne.append(bytes_to_list(cconn[i][0].recv(1024)))
          if(colonne in dati_attributi ):
              
                cconn[i][0].send("Inserisci il valore che vuoi eliminare nella tabella\n".encode())
                
                risp3=bytes_to_list(cconn[i][0].recv(1024))
              
                query=f"DELETE  FROM {tabella} WHERE {colonne}={risp3}"
                cur.execute(query)
                cconn[i][0].send("Elementi eliminati\n".encode())
                
          elif(colonne not in dati_attributi ):
              cconn[i][0].send("L'attributo non esiste".encode())
              
              cconn[i][0].close()
              

          
      else:
            cconn[i][0].send("Inserimento errato riprovare".encode())
            
            cconn[i][0].close()
    
#----------------------------------------------------------------------------------------------------------------------------------
   
def connessioni(conn,i,lock):
    
    tentativi = 3
    risp = 0
    lock.acquire()
    while tentativi > 0:
        conn[i][0].send("Inserisci la password\n".encode())
        data = conn[i][0].recv(1024).decode()

        if data != "1234":
            conn[i][0].send("Hai sbagliato la password".encode())
            tentativi -= 1

            if tentativi == 0:
                conn[i][0].send("Hai esaurito i tentativi, connessione interrotta".encode())
                conn[i][0].close()
                
                break
                

        elif data == "1234":
            risp = 0  # Inizializzazione di risp
            while risp not in ("1", "2", "3", "4"):
                conn[i][0].send("Cosa vuoi fare\n1-Inserire\n2-Leggere\n3-Modificare\n4-Eliminare".encode())
                risp = conn[i][0].recv(1024).decode()
                
            db(conn,i,risp)

            
            
            
            break
            

    lock.release()            
#----------------------------------------------------------------------------------------------------------------------------------

print("Server in ascolto: ")

lock = threading.Lock()
HOST = '127.0.0.1'
PORT = 50010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
conne = []
i=0
while True:
    conn, addr = s.accept()
    conne.append((conn, addr))

    thread = threading.Thread(target=connessioni, args=(conne,i, lock))
    thread.start()
    i=i+1