import socket
import logging

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)

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

        while True:
            data = c_sock.recv(2048)
            log.warning(f'Received: {data}')
            if not data:
                break
            else:
                c_sock.send(b'Got data')

if __name__ == '__main__':
    main()