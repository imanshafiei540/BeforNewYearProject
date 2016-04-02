import socket
network = socket.socket()
host = '0.0.0.0'
port = 5001
network.bind((host, port))
network.listen(5)
connection = True
while connection:
    client, addr = network.accept()
    user = client.recv(1024)
    password = client.recv(1024)
    print user
    print password

    if (user == "i m a n " or password == "1 2 3 "):
        client.send('1')
    else:
        client.send('0')
