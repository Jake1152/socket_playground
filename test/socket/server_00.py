import socket

HOST = ''
PORT = 8000
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Server listening on port {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                conn.sendall(data)
                print(f"Received and sent back: {data.decode()}")
if __name__ == "__main__":
    main()