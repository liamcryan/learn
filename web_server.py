# from let's build a web server. part 1 (ruslan's blog)
import re
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print('serving http on port {}'.format(PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)
    if request[4:request.find(b'HTTP')-1].rfind(b'shutdown') > -1:
        http_response = b'HTTP/1.1 200 OK\n\nShutting Down...'
        client_connection.sendall(http_response)
        client_connection.close()
        break

    http_response = b'HTTP/1.1 200 OK\n\n' + request
    client_connection.sendall(http_response)
    client_connection.close()
