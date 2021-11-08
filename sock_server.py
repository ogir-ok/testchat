import threading
import socket
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


CLIENTS = set()

class ClientThread(threading.Thread):
    def __init__(self, client_socket, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_socket = client_socket

    def run(self):
        while True:
            data = self.client_socket.recv(2048)
            log.warning(f'Received: {data}')
            if not data:
                CLIENTS.remove(self.client_socket)
                break
            else:
                for client in CLIENTS:
                    if client != self.client_socket:
                        client.send(data)


def create_server_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.bind(('0.0.0.0', 5001))
    sock.listen()

    return sock

def main():
    log.warning('Hi!')

    s_sock = create_server_socket()

    while True:
        c_sock, addr = s_sock.accept()
        log.warning(f'Connected from addr {addr}')
        CLIENTS.add(c_sock)
        client_thread = ClientThread(c_sock)
        client_thread.start()


if __name__ == '__main__':
    main()