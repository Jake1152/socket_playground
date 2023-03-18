import socket

HOST = "localhost"
PORT = 8000
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connected to {HOST}: {PORT}")
        while True:
            message = input("Enterh message to send (or 'exit' to quit): ")
            if message == 'exit':
                break
            s.sendall(message.encode())
            data = s.recv(BUFFER_SIZE)
            print(f"Received from server : {data.decode()}")

if __name__ == "__main__":
    main()
