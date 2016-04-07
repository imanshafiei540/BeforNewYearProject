import socket
import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *



def toList(path, step , stepmax=2):
    directory =[]
    try:
        if(step<=stepmax ):
            l = os.listdir(path)

            for i in l:
                filename = path+'/'+ i
                if(not os.path.isfile(filename)):
                    newlist = ( i , toList(filename,step+1,stepmax))
                    directory.append(newlist)
                else:
                    newlist = (i , [])
                    directory.append(newlist)

        return directory

    except WindowsError:
        return None

print exit

data = toList('C:\Users\Administrator\Desktop',1 ,  5)
print 1



network = socket.socket()
host = '0.0.0.0'
port = 5003
network.bind((host, port))
network.listen(5)
connection = True

file = open('passdict.txt', 'r')
info = file.readlines()
info = eval(info[0])

while connection:
    client, addr = network.accept()
    client.send(str(len(str(data))))
    receive = client.recv(4)
    user = client.recv(1024)
    password = client.recv(1024)
    print user in info
    print info[user] == password
    if (user in  info) and (info[user] == password):
        client.send('accepted')


    if receive== "True":
        print "###############"
        client.send(str(data))



