from socket import *
import random

port = 3333
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print(f"[INFO] UDP Server listening on port {port}...")

while True:
    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)
    received = data.decode()
    reTx, message = received.split(' ', 1)
    print(f'<- {reTx} {message}')

    # 40% 확률로 손실 (응답하지 않음), 60% 확률로 ack 전송
    if random.random() <= 0.4:
        continue
    else:
        sock.sendto(b'ack', addr)
        # 에코 응답 전송
        resp = f'{reTx} {message}'
        sock.sendto(resp.encode(), addr)

sock.close()