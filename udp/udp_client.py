from socket import *
import time

server_addr = ('127.0.0.1', 3333)
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        sock.sendto(f'{reTx} {msg}'.encode(), server_addr)
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break
        except timeout:
            reTx += 1
            if reTx > 5:
                print('Max retransmissions reached. Exiting.')
                exit()
            continue

    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)
    received = data.decode()
    reTx, message = received.split(' ', 1)
    print(f'<- {reTx} {message}')