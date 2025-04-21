import socket

# 서버 설정
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print('Enter the message("send mboxId message" or "receive mboxId"):')
    msg = input("> ").strip()
    sock.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))

    if msg == "quit":
        break

    data, _ = sock.recvfrom(BUFFER_SIZE)
    print(data.decode())

sock.close()
