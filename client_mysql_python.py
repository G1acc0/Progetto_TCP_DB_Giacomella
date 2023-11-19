import socket

HOST = 'localhost'
PORT = 50010

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        data = s.recv(1024)
        if not data:
            break

        print('Received:', data.decode())
        
        user_input = input("Enter text to send (type 'exit' to quit): ")
        s.send(user_input.encode())

        if user_input.lower() == 'exit':
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    s.close()
