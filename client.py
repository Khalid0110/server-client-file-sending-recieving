#!/use/bin/python3
## Khalid Abdulmejid, Muhammed ITIR
## 1611012095, 1611012096
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 300

client_socket.connect((host, port))

message1 = client_socket.recv(1024)
message2 = client_socket.recv(1024)

print(message1.decode('ascii'))

with open("recieved.txt","w") as recf:
    recf.write(message2)
    recf.close()
    print("the response is stored in a file <recieved.txt>")


	
	

