import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 3333))

while True:
    msg = input("계산식 입력: ")
    if msg == 'q':
        print("종료")
        break
    try:
        s.send(msg.encode())
        data = s.recv(1024)
        print(msg, "=", data.decode())
    except:
        break
s.close()