import Pyro4
import base64
import json
import sys

namainstance = sys.argv[1] or "fileserver"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()

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