import socket

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

mailboxes = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"[INFO] UDP Server listening on {HOST}:{PORT}...")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    message = data.decode().strip()
    
    if message == "quit":
        print("[INFO] Server shutting down...")
        break

    elif message.startswith("send "):
        parts = message.split(' ', 2)
        if len(parts) < 3:
            sock.sendto("Invalid format".encode(), addr)
            continue
        mbox_id, msg = parts[1], parts[2]
        if mbox_id not in mailboxes:
            mailboxes[mbox_id] = []
        mailboxes[mbox_id].append(msg)
        sock.sendto("OK".encode(), addr)

    elif message.startswith("receive "):
        parts = message.split(' ', 1)
        if len(parts) < 2:
            sock.sendto("Invalid format".encode(), addr)
            continue
        mbox_id = parts[1]
        if mbox_id in mailboxes and mailboxes[mbox_id]:
            response = mailboxes[mbox_id].pop(0)
            sock.sendto(response.encode(), addr)
        else:
            sock.sendto("No messages".encode(), addr)
    else:
        sock.sendto("Invalid command".encode(), addr)

sock.close()