import os
import base64
import random

class FileServer(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name='filename000'):
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(nama))
        try:
            f = open(nama,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
    def update(self,name='filename000',content=''):
        nama='FFF-{}' . format(name)
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(nama,'w+b')
            f.write(content.encode())
            f.close()
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')

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
                    os.exit(1)
            time.sleep(2)
            
    def central_heartbeat(self,client_seq,id_client):
        global seq
        try:
            if seq[str(id_client)]==client_seq:
                seq[str(id_client)]+=1
                client_seq+=1
                return client_seq
        except Exception as e:
            seq[str(id_client)]=0
            return 0

    def all_heartbeat(self,client_seq, id_client):
        global seq
        try:
            if seq[str(id_client)]==client_seq:
                seq[str(id_client)]+1
                client_seq+=1
                return client_seq,seq
        except Exception as e:
            seq[str(id_client)]=0
            return 0, seq

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

