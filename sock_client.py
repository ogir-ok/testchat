import threading
import socket
from time import sleep
import logging

USERNAME = 'ogir_ok'

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)

def create_client_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('116.203.224.72', 5001))
    return sock


class SockThread(threading.Thread):
    def __init__(self, sock, *a, **kwa):
        super().__init__(*a, **kwa)
        self.sock = sock


class ReaderThread(SockThread):
    def run(self):
        while True:
            message = input(f'<{USERNAME}>:')
            self.sock.send(f'<{USERNAME}>:{message}'.encode())


class WriterThread(SockThread):
    def run(self):
        while True:
            response = self.sock.recv(2048)
            print('\r' + response.decode())
            print(f'<{USERNAME}>:', end='')


def func():
    message = input()
    print(message)

def main():
    log.warning('Starting client')
    sock = create_client_socket()
    log.warning(f'Connected to {sock}')

    ReaderThread(sock).start()
    WriterThread(sock).start()


if __name__ == '__main__':
    main()