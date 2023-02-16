import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('10.13.0.16', 3131))
server_socket.listen() 

while(True):
    with open('cmds.txt', 'r') as cmd:
            if cmd.readline() != 'stop':
                    client_connected, client_address = server_socket.accept()
                    print(f"Connection request accepted from {client_address[0]},{client_address[1]}")

                    write_file = open(f'{client_address[0]}.data.txt', 'wb')
                    print('Write file opened!')

                    client_data = client_connected.recv(2048)
                    print('Data received')

                    while len(client_data)>0: 
                        write_file.write(client_data)
                        client_data = client_connected.recv(2048)
                    write_file.close()
                    print('File written!')
            else: break

server_socket.close()