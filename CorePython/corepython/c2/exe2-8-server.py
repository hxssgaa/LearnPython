from twisted.internet import protocol, reactor

PORT = 50008


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):  # A method that is executed when a client connects to us
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):  # Called when a client sends a piece of data across the network
        print("data received:%s" % data.decode('utf-8'))
        ipt = input("> ")
        self.transport.write(bytes(ipt, 'utf-8'))


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
