from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.bind((host, port))
    s.listen(5)
    print("Server is listening on port", port)
    
    client, addr = s.accept()
    print("Connection from", addr[0])
    
    while True:
        x = client.recv(2048)
        if not x:
            break  # Exit loop if client disconnects
        print("client:", x.decode('utf-8'))
        y = input("server: ")
        client.send(y.encode('utf-8'))
except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is terminated")
finally:
    client.close()
    s.close()
