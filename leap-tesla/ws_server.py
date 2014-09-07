from autobahn.twisted.websocket import WebSocketServerProtocol
from autobahn.twisted.websocket import WebSocketServerFactory, listenWS

class MyServerProtocol(WebSocketServerProtocol):

   def onConnect(self, request):
      print("Client connecting: {}".format(request.peer))

   def onOpen(self):
      print("WebSocket connection open.")
      self.factory.register(self)

   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {} bytes".format(len(payload)))
      else:
         print("Text message received: {}".format(payload.decode('utf8')))

      ## echo back message verbatim
      self.factory.broadcast(payload)

   def onClose(self, wasClean, code, reason):
      print("WebSocket connection closed: {}".format(reason))

class BroadcastServerFactory(WebSocketServerFactory):
   def __init__(self, url, debug = False, debugCodePaths = False):
      WebSocketServerFactory.__init__(self, url, debug = debug, debugCodePaths = debugCodePaths)
      self.clients = []
      self.tickcount = 0

   def tick(self):
      self.tickcount += 1
      self.broadcast("tick %d from server" % self.tickcount)
      reactor.callLater(1, self.tick)

   def register(self, client):
      if not client in self.clients:
         print("registered client {}".format(client.peer))
         self.clients.append(client)

   def unregister(self, client):
      if client in self.clients:
         print("unregistered client {}".format(client.peer))
         self.clients.remove(client)

   def broadcast(self, msg):
      print("broadcasting message '{}' ..".format(msg))
      for c in self.clients:
         c.sendMessage(msg.encode('utf8'))
         print("message sent to {}".format(c.peer))


def main():
   import sys

   from twisted.python import log
   from twisted.internet import reactor
   log.startLogging(sys.stdout)

   
   factory = BroadcastServerFactory("ws://localhost:9000")
   factory.protocol = MyServerProtocol

   reactor.listenTCP(9000, factory)

   reactor.run()

if __name__ == '__main__':
   main()
