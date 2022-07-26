import socket;

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("CLIENT SIDE")

try:
        client.connect((HOST,SERVER_PORT))
        print("client address: ",client.getsockname())

        request = input("Request of client: ")
        client.sendall(request.encode(FORMAT))
        
        print("khách đã nhận được menu")
        H1 = client.recv(1024).decode(FORMAT)
        print(H1)
        sp = (input())
        client.sendall(sp.encode(FORMAT))
        H2 = client.recv(1024).decode(FORMAT)
        print(H2)
        sb = (input())
        client.sendall(sb.encode(FORMAT))
        H3 = client.recv(1024).decode(FORMAT)
        print(H3)
        sf = (input())
        client.sendall(sf.encode(FORMAT))
        H4 = client.recv(1024).decode(FORMAT)
        print(H4)
        sh = (input())
        client.sendall(sh.encode(FORMAT))
        H5 = client.recv(1024).decode(FORMAT)
        print(H5)
        st = (input())
        client.sendall(st.encode(FORMAT))
        
        Sum = client.recv(1024).decode(FORMAT)
        print("tong la: "+ Sum)
        P = client.recv(1024).decode(FORMAT)
        print(P)
        
        
        n1 = (input())
        client.sendall(n1.encode(FORMAT))

        
        if int(n1) == 1:
                Cxstk = client.recv(1024).decode(FORMAT)
                print(Cxstk)
                Stk = (input())
                client.sendall(Stk.encode(FORMAT))
        else:
                Tm = (input())
                client.sendall(Tm.encode(FORMAT))

except:
        print("Error")

