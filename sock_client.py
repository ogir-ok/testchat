import socket
from time import sleep
import logging

USERNAME = 'Client'

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)

def create_client_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('server', 5001))
    return sock

def main():
    log.warning('Starting client')
    sock = create_client_socket()
    log.warning(f'Connected to {sock}')

    while True:
        sock.send(f"{USERNAME}: I'm a client".encode())
        response = sock.recv(2048)
        log.warning(f'Response: {response}')

        sleep(10)


if __name__ == '__main__':
    main()