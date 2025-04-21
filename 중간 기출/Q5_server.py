import socket

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

mailboxes = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[INFO] TCP Server listening on {HOST}:{PORT}...")

while True:
    connection_socket, addr = server_socket.accept()
    print(f"[INFO] Connected to client {addr}")

    while True:
        try:
            data = connection_socket.recv(BUFFER_SIZE).decode().strip()
            if not data:  # 클라이언트 연결 종료 처리
                print(f"[INFO] Client {addr} disconnected")
                break

            if data == "quit":
                print(f"[INFO] Client {addr} sent quit")
                break

            elif data.startswith("send "):
                parts = data.split(' ', 2)
                if len(parts) < 3:
                    connection_socket.send("Invalid format".encode())
                    continue
                mbox_id, msg = parts[1], parts[2]
                if mbox_id not in mailboxes:
                    mailboxes[mbox_id] = []
                mailboxes[mbox_id].append(msg)
                connection_socket.send("OK".encode())

            elif data.startswith("receive "):
                parts = data.split(' ', 1)
                if len(parts) < 2:
                    connection_socket.send("Invalid format".encode())
                    continue
                mbox_id = parts[1]
                if mbox_id in mailboxes and mailboxes[mbox_id]:
                    response = mailboxes[mbox_id].pop(0)
                    connection_socket.send(response.encode())
                else:
                    connection_socket.send("No messages".encode())
            else:
                connection_socket.send("Invalid command".encode())

        except ConnectionResetError:
            print(f"[INFO] Client {addr} disconnected unexpectedly")
            break

    connection_socket.close()

server_socket.close()

# SOCK_STREAM으로 TCP 소켓 생성.
# listen()과 accept()로 클라이언트 연결 수락, 각 연결마다 새로운 connection_socket 사용.
# 외부 while True로 새로운 클라이언트 연결 대기, 내부 루프에서 단일 클라이언트의 메시지 처리.
# "quit" 수신 시 현재 클라이언트 연결만 종료하고, 서버는 계속 실행.
# ConnectionResetError 처리로 클라이언트의 비정상 종료 대응.
# UDP의 sendto/recvfrom 대신 TCP의 send/recv 사용, 주소 정보 불필요.