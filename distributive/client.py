import socket
def webscrape(ids):
    import find_users
    id1 = ''
    id2 = ''
    next = False
    for id in ids:
        if id != ',':
            if not next:
                id1 = id1 + id
            if next:
                id2 = id2 + id
        else:
            next = True
    print(id1, id2)
            
    print(ids)
    init_vals = find_users.client_initialize(int(id1), int(id2))
    f = find_users.client_main(init_vals[0], init_vals[1], init_vals[2])
    print("Finished finding users!\n\n")
    return f

def send_data(f):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.13.0.16', 3131))

    data_to_upload = open(f, 'rb')
    data_chunk = data_to_upload.read(2048)
    while data_chunk:
        client_socket.send(data_chunk)
        data_chunk = data_to_upload.read(2048)
    print('Data transmitted!')
    data_to_upload.close()
    client_socket.close()

def get_command():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.13.0.16', 3131))

    command = client_socket.recv(20).decode()
    print('Received command!')
    return command

def main():
    ids = get_command()
    filename = webscrape(ids)
    send_data(filename)

if __name__=="__main__":
    main()