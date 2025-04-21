import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"[INFO] Connected to server {SERVER_HOST}:{SERVER_PORT}")

while True:
    print('Enter the message ("send mboxId message" or "receive mboxId"):')
    msg = input("> ").strip()
    client_socket.send(msg.encode())

    if msg == "quit":
        print("[INFO] Closing connection")
        break

    data = client_socket.recv(BUFFER_SIZE).decode()
    print(data)

client_socket.close()

# TCP 소켓으로 서버에 연결 후, UDP와 동일한 입력/출력 로직 유지.
# 메시지 전송 후 서버 응답 수신, "quit" 입력 시 연결 종료.
# UDP의 sendto 대신 send, 주소 지정 불필요.