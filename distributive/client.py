### TODO Implement webscraper (easy)
def webscrape():
    import find_users
    find_users.main()
    print("Finished finding users!\n\n")

def send_data():
    import socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.13.0.16', 3131))

    filename = 'data.txt'

    image_to_upload = open(filename, 'rb')
    image_chunk = image_to_upload.read(2048)
    while image_chunk:
        client_socket.send(image_chunk)
        image_chunk = image_to_upload.read(2048)
    print('Data transmitted!')
    image_to_upload.close()
    client_socket.close()