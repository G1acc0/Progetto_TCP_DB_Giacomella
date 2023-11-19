import socket
import mysql.connector
import threading
def db(cconn,i,risp):
    tabelle={'dipendenti':'dipendenti_marco_giacomella','zone':'zone_di_lavoro_marco_giacomella'}
    colonne=[]
    conn = mysql.connector.connect(
                    host="127.0.0.1", # 10.10.0.10
                    user="marco_giacomella",
                    password="giacomella1234",
                    database="5BTepsit",
                    port=3306, 
                    )
    cur = conn.cursor()
#---------------------------------------------------------------------------------------------------------------------------
    if risp == 1:
      cconn[i][0].send("Inserisci la tabella su cui vuoi inserire: ".encode())
      tabella_scelta = cconn[i][0].recv(1024).decode()

      if tabella_scelta in tabelle:
          tabella = tabelle[tabella_scelta]
          query_colonne = f"SHOW COLUMNS FROM {tabella}"

          try:
              cur.execute(query_colonne)
              colonne = [col[0] for col in cur.fetchall()]
              cconn[i][0].send(f"Le colonne da inserire sono queste: {colonne}\n".encode())
              risp3 = cconn[i][0].recv(1024).decode()

              # Usare parametri per prevenire SQL injection
              query_inserimento = f"INSERT INTO {tabella} VALUES ({', '.join(['%s' for _ in colonne])})"
              cur.execute(query_inserimento, tuple(risp3.split(',')))
              conn.commit()

              cconn[i][0].send("Inserimento riuscito\n".encode())
          except mysql.connector.Error as err:
              cconn[i][0].send(f"Errore durante l'inserimento: {err}\n".encode())
      else:
          cconn[i][0].send("Tabella non valida\n".encode())

#----------------------------------------------------------------------------------------------------------------------------------


    if risp==2:
      cconn[i][0].send("Inserisci la tabella sul quale vuoi inserire").encode()
      risp2=cconn[i][0].recv(1024).decode()
      if(risp2 in tabelle.keys()):
          tabella=tabelle.get(risp2)
          query = f"SHOW COLUMNS FROM {tabella}"
          try:
            cur.execute(query)
          except Exception:
            cconn[i][0].send("Tabella non corretta - MYSQL Error").encode()
            cconn[i][0].close()
        

          dati = cur.fetchall()
          dati_attributi=[]
          for riga in dati:
            dati_attributi.append(riga[0])
          cconn[i][0].send(f"Le colonne che si possono leggere sono queste {dati_attributi} quali vuoi leggere\n").encode()
          colonne.append(cconn[i][0].recv(1024).decode())
          if(colonne in dati_attributi or colonne=='*'):
              if(colonne=='*'):
                  query=f"SELECT {colonne} FROM {tabella} "
                  cur.execute(query)
                  dati=cur.fetchall()
                  print(dati)
              else:
                cconn[i][0].send("Inserisci il valore che vuoi confermare nella tabella\n").encode()
                risp3=cconn[i][0].recv(1024).decode()
              
                query=f"SELECT {colonne} FROM {tabella} where {colonne}={risp3}"
                cur.execute(query)
                dati=cur.fetchall()
                print(dati)
          elif(colonne not in dati_attributi ):
              cconn[i][0].send("L'attributo non esiste").encode()

          
      else:
            cconn[i][0].send("Inserimento errato riprovare").encode()

#----------------------------------------------------------------------------------------------------------------------------------



    if risp==3:
      cconn[i][0].send("Inserisci la tabella sul quale vuoi eliminare").encode()
      risp2=cconn[i][0].recv(1024).decode()
      if(risp2 in tabelle.keys()):
          tabella=tabelle.get(risp2)
          query = f"SHOW COLUMNS FROM {tabella}"
          try:
            cur.execute(query)
          except Exception:
            cconn[i][0].send("Tabella non corretta - MYSQL Error").encode()
        

          dati = cur.fetchall()
          dati_attributi=[]
          for riga in dati:
            dati_attributi.append(riga[0])
          cconn[i][0].send(f"Le colonne dove si può eliminare sono queste {dati_attributi} quali vuoi leggere\n").encode()
          colonne.append(cconn[i][0].recv(1024).decode())
          if(colonne in dati_attributi ):
              
                cconn[i][0].send("Inserisci il valore che vuoi modificare nella tabella\n").encode()
                risp3=cconn[i][0].recv(1024).decode()
                cconn[i][0].send("Inserisci il valore che vuoi inserire nella tabella\n").encode()
                risp4=cconn[i][0].recv(1024).decode()
                query=f"UPDATE {tabella}  SET {risp4} where {colonne}={risp3}"
                cur.execute(query)
                cconn[i][0].send("Elementi aggiornati\n").encode()
          elif(colonne not in dati_attributi ):
              cconn[i][0].send("L'attributo non esiste").encode()
              cconn[i][0].close()

          
      else:
            cconn[i][0].send("Inserimento errato riprovare").encode()
            cconn[i][0].close()


#----------------------------------------------------------------------------------------------------------------------------------

    if risp==4:
      cconn[i][0].send("Inserisci la tabella sul quale vuoi eliminare").encode()
      risp2=cconn[i][0].recv(1024).decode()
      if(risp2 in tabelle.keys()):
          tabella=tabelle.get(risp2)
          query = f"SHOW COLUMNS FROM {tabella}"
          try:
            cur.execute(query)
          except Exception:
            cconn[i][0].send("Tabella non corretta - MYSQL Error").encode()
            cconn[i][0].close()
        

          dati = cur.fetchall()
          dati_attributi=[]
          for riga in dati:
            dati_attributi.append(riga[0])
          cconn[i][0].send(f"Le colonne dove si può eliminare sono queste {dati_attributi} quali vuoi leggere\n").encode()
          colonne.append(cconn[i][0].recv(1024).decode())
          if(colonne in dati_attributi ):
              
                cconn[i][0].send("Inserisci il valore che vuoi confermare nella tabella\n").encode()
                risp3=cconn[i][0].recv(1024).decode()
              
                query=f"DELETE {colonne} FROM {tabella} where {colonne}={risp3}"
                cur.execute(query)
                cconn[i][0].send("Elementi eliminati\n").encode()
          elif(colonne not in dati_attributi ):
              cconn[i][0].send("L'attributo non esiste").encode()
              cconn[i][0].close()
              

          
      else:
            cconn[i][0].send("Inserimento errato riprovare").encode()
            cconn[i][0].close()
    
#----------------------------------------------------------------------------------------------------------------------------------
   
def connessioni(conn,i,lock):
    lock.acquire()
    tentativi=3
    risp=0
    while(tentativi>0):
      
      conn[i][0].send("Inserisci la password\n".encode())
      data=conn[i][0].recv(1024).decode()
      if(data!="1234"):
        
                conn[i][0].send("Hai sbagliato la password")
                tentativi-=1
                if(tentativi==0):
                    conn[i][0].send("Hai esaurito i tentativi connessione interrota")
                    conn[i][0].close()
                    
    

     
      if(data=="1234"):
                while(risp!="1" or risp!="2" or risp!="3" or risp!="4"):
                    conn[i][0].send("Cosa vuoi fare 1-Inserire\n2-Leggere\n3-Modificare\n4-Eliminare".encode())
                    risp=conn[i][0].recv(1024).decode()
        
                db(conn,i,risp)
                break
                
      elif(risp not in ("1","2","3","4")):
                    conn[i][0].send("Inserimento errato".encode())
                    break
  
                
                    
    lock.release()
            
                
                
            
#----------------------------------------------------------------------------------------------------------------------------------
      
print("server in ascolto: ")
lock = threading.Lock()
HOST = '127.0.0.1'
PORT = 50010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
con = []
i = 0
conne = []
while True:
    # il server si stoppa qui in attesa di dati dal client
    conne.append(s.accept())
    
    con.append(threading.Thread(target=connessioni,args=(conne,i,lock)))
    try:
      con[i].start()
    except:
      print("errore")
    
    i+=1
    
con.close()   
