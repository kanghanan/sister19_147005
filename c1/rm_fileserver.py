serverlist=[]

class FileServer(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def add_server(self, server_name):
        serverlist.append(server_name)

    def get_serverlist(self):
        return serverlist

    def another_server(self, servername):
        uri = "PYRONAME:{}@localhost:7777".format(servername)
        replserver = Pyro4.Proxy(uri)
        return replserver

    def consistency(self, from_server, command, filename, content=None):
        if command == "create":
            for server in serverlist:
                if str(server) != str(from_server):
                    print(str(server))
                    fserver = self.another_server(server)
                    fserver.create(filename, 0)
                    # self.create(filename,server)
        elif command == 'delete':
            for server in serverlist:
                if str(server) != str(from_server):
                    fserver = self.another_server(server)
                    fserver.delete(filename, 0)
                    # self.delete(filename,server)
        elif command == 'update':
            for server in serverlist:
                if str(server) != str(from_server):
                    fserver = self.another_server(server)
                    fserver.update(filename, content, 0)
                    # self.update(filename,content,server)
        return "ok"

if __name__ == '__main__':
    k = FileServer()
    print(k.create('f1'))
    print(k.update('f1',content='wedusku'))
    print(k.read('f1'))
#    print(k.create('f2'))
#    print(k.update('f2',content='wedusmu'))
#    print(k.read('f2'))
    print(k.list())
#print(k.delete('f1'))