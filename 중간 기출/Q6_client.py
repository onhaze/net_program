from socket import *
import time

server_addr = ('127.0.0.1', 3333)
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 3:  # 최대 3회 재전송 (총 4회 전송)
        sock.sendto(f'{reTx} {msg}'.encode(), server_addr)
        sock.settimeout(1)  # 1초 타임아웃
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break
        except timeout:
            reTx += 1
            if reTx > 3:
                print('Max retransmissions reached. Exiting.')
                exit()
            continue

    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)
    received = data.decode()
    reTx, message = received.split(' ', 1)
    print(f'<- {reTx} {message}')

sock.close()