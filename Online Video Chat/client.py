#!/usr/bin/python
import socket, videosocket
import io
from videofeed import VideoFeed

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 6000))
        self.vsock = videosocket.videosocket (self.client_socket)
        self.videofeed = VideoFeed(1,"client",1)
        self.data=StringIO.StringIO()

    def connect(self):
        while True:
            frame=self.videofeed.get_frame()
            self.vsock.vsend(frame)
            frame = self.vsock.vreceive()
            self.videofeed.set_frame(frame)
            
#            print "RECIEVED:" , frame
        """if (data <> 'Q' and data <> 'q'):
            self.client_socket.send(data)
        else:
            self.client_socket.send(data)
            self.client_socket.close()
            break;
            """
                
if __name__ == "__main__":
    client = Client()
    client.connect()
