from autobahn.twisted.websocket import WebSocketClientProtocol

class LeapClientProtocol(WebSocketClientProtocol):

    def __init__(self):
        super(LeapClientProtocol, self).__init__()
        self.websocket_version = 0

    def onOpen(self):
        self.sendMessage(u"Hello, world!".encode('utf8'))

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))