import socket;
import sys
import json
def main():
    start()

def start():
    #serverlist = []
    HOST = "127.0.0.1"
    SERVER_PORT = 65432
    FORMAT = "utf8"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    s.bind((HOST,SERVER_PORT))
    s.listen(5);

    print("SERVER SIDE")
    print("server: ",HOST, SERVER_PORT)
    print("waiting for client")

    try:
        con, addr = s.accept()
        print("client address: ",addr)
        print("Hệ thống xin chào")
        
        request = con.recv(1024).decode(FORMAT)
        print("Request of client: ",request)
        
        if request == 'menu':
            with open('data.json') as f:    
                data = json.load(f)   
            for food in data:
                print("Menu có {} giá {}" .format(food['food'], food['price'], food['note'], food['image']))
            f.close()
        H1 = "Quý khách đặt bao nhiêu Pizza"
        con.sendall(H1.encode(FORMAT))
        sp = con.recv(1024).decode(FORMAT)
        H2 = "Quý khách đặt bao nhiêu Chicken"
        con.sendall(H2.encode(FORMAT))
        sc = con.recv(1024).decode(FORMAT)
        H3 = "Quý khách đặt bao nhiêu Fish"
        con.sendall(H3.encode(FORMAT))
        sf = con.recv(1024).decode(FORMAT)
        H4 = "Quý khách đặt bao nhiêu Hotpot"
        con.sendall(H4.encode(FORMAT))
        sh = con.recv(1024).decode(FORMAT)
        H5 = "Quý khách đặt bao nhiêu Takoyaki"
        con.sendall(H5.encode(FORMAT))
        st = con.recv(1024).decode(FORMAT)

        a = int(sp) * 50000 + int(sc) * 35000 + int(sf) * 35000 + int(sh) * 35000 + int(st) * 35000
        Sum = "% s" % a
        con.sendall(Sum.encode(FORMAT))

        data_dict = {}
        data_dict['cus']=[]
        data_dict['cus'].append({"pizza":sp})
        data_dict['cus'].append({"chicken":sc})
        data_dict['cus'].append({"fish":sf})
        data_dict['cus'].append({"hotpot":sh})
        data_dict['cus'].append({"takoyaki":st})

        with open("info.json", 'w') as file:
            json.dump(data_dict, file)
        file.close()

        print("Lựa chọn cách thanh toán"'\n'"Nhấn 1: nếu muốn thanh toán bằng thẻ"'\n'"Nhấn 2: nếu muốn thanh toán bằng tiền mặt")
        n1 = con.recv(1024).decode(FORMAT)
        print(n1)
        if int(n1) == 1:
            Cxstk = "Số tài khoản của quý khách là: "
            Stk = con.recv(1024).decode(FORMAT)
            if len(Stk) == 5 and Stk.isnumeric():
                print("Thành công")
            else:
                print ("Thất bại-Bạn hãy nhập lại")
                Cxstk = "Số tài khoản của quý khách là: "
                Stk = con.recv(1024).decode(FORMAT)
        if int(n1) == 2:
            Cxstk = "Số tiền mặt quý khách phải trả là: "
            Tm = con.recv(1024).decode(FORMAT)
            if int(Tm) >= Sum:
                Tt = Sum - Tm
                print ("Số tiền thừa là: " + Tt)
            else:
                print ("Không thể thanh toán")
    except:
        print ("Error")

if __name__ == "__main__":
    main()