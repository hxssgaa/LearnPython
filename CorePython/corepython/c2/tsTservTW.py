from time import ctime

from twisted.internet import protocol, reactor

PORT = 21567


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):  # A method that is executed when a client connects to us
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):  # Called when a client sends a piece of data across the network
        self.transport.write(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
