from socket import *

def calculate(msg):
    try:
        msg = msg.replace(" ", "")
        result = eval(msg, {"__builtins__": None}, {})
        return str(round(result, 1) if isinstance(result, float) else result)
    except Exception as e:
        return "Error"

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", 3333))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print("Connected by", remotehost, remoteport)

while True:
    try:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print("Received msg:", msg)
        result = calculate(msg)
        conn.send(result.encode())
    except:
        break

conn.close()
