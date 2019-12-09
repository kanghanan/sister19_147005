import Pyro4
import base64
import json
import sys
import threading
import time
import os
import uuid


namainstance = sys.argv[1] or "fileserver"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver
def ping(name):
    count=0
    while True:
        try:
            ns = Pyro4.locateNS("localhost",7777)
            count=0
        except Exception as e:
            count+=1
            print("\nserver down count "+str(count))
            if count>2:
                os._exit(1)
        time.sleep(2)

def centralized_heartbeat(i,myid):
    global seq
    count=0
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    while True:
        try:
            uri = "PYRONAME:greetserver@localhost:7777"
            gserver = Pyro4.Proxy(uri)
            seq=gserver.centralized_heartbeat(seq,myid)
            print("seq "+str(seq))
        except Exception as e:
            count+=1
            print("Server is Down")
            if count>2:
                os._exit(1)
        time.sleep(2)

def `(i,myid):
    global seq
    count=0
    uri="PYRONAME.greetserver@localhost:7777"
    gserver=Pyro4.Proxy(uri)
    while True:
        try:
            uri="PYRONAME.greetserver@localhost:7777"
            gserver=Pyro4.Proxy(uri)
            seq,all_client_seq=gserver.all_hearbeat(seq,myid)
            print("All Client Seq: \n"+str(all_client_seq))
        except Exception as e:
            count+=1
            print("Server is Down")
            if count>2:
                os._exit(1)
        time.sleep(2)

if __name__=='__main__':
    f = get_fileserver_object()
    opsi=input("Failure detection: ")
    if opsi==1:
        x = threading.Thread(target=ping, args=(1,))
        x.start()
    elif opsi==2:
        myid=uuid.uuid4()
        x = threading.Thread(target=centralized_heartbeat, args=(1,myid))
        x.start()
    elif opsi==3
        myid=uuid.uuid4()
        x = threading.Thread(target=a2a_heartbeat, args=(1,myid))
        x.start()

    while True:
        command = input ("Command : ")
        command = command.split(" ")
        if command[0]=="list":
            print(f.list())
        elif command[0]=="create":
            f.create(command[1])
        elif command[0]=="update":
            f.update(command[1], content = open(command[1],'rb+').read() )
        elif command[0]=="read":
            d=f.read(command[1])
            string='decode_'
            string+=command[1]
            open(string,'w+b').write(base64.b64decode(d['data']))
        elif command[0]=="delete":
            f.delete(command[1])