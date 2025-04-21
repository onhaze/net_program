import socket

# 릴레이 서버 설정
RELAY_HOST = 'localhost'
RELAY_PORT = 9000
EXTERNAL_HOST = 'www.daum.net'
EXTERNAL_PORT = 80
BUFFER_SIZE = 4096

def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((RELAY_HOST, RELAY_PORT))
    server_socket.listen(1)
    print(f"[INFO] Relay server listening on {RELAY_HOST}:{RELAY_PORT}...")
    return server_socket

def create_external_socket():
    external_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    external_socket.connect((EXTERNAL_HOST, EXTERNAL_PORT))
    return external_socket

def handle_client(client_socket):
    # 브라우저로부터 HTTP 요청 수신
    request = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    if not request:
        client_socket.close()
        return

    # 요청 라인(첫 줄) 추출
    request_lines = request.split('\n')
    request_line = request_lines[0].strip()

    # 외부 서버로 보낼 HTTP 요청 생성 (요청 라인 + Host 헤더)
    http_request = f"{request_line}\r\nHost: {EXTERNAL_HOST}\r\n\r\n"

    # 외부 서버에 연결 및 요청 전송
    external_socket = create_external_socket()
    external_socket.send(http_request.encode('utf-8'))

    # 외부 서버로부터 응답 수신
    response = b""
    while True:
        data = external_socket.recv(BUFFER_SIZE)
        if not data:
            break
        response += data

    # 외부 서버 소켓 종료
    external_socket.close()

    # 브라우저로 응답 전달
    client_socket.send(response)

    # 클라이언트 소켓 종료
    client_socket.close()

def main():
    server_socket = create_server_socket()
    
    while True:
        try:
            client_socket, addr = server_socket.accept()
            print(f"[INFO] Accepted connection from {addr}")
            handle_client(client_socket)
        except KeyboardInterrupt:
            print("\n[INFO] Shutting down relay server...")
            server_socket.close()
            break

if __name__ == "__main__":
    main()