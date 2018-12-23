# coding: utf-8
from twisted.internet import protocol, reactor

class Knock(object):
	def dataReceived(self, data):
		print("Client:", data)
		if data.startswitch(str("knock knock")):
			response = "Who's there?"
		else:
			response = data + "who?"
		print("Server:", response)
		self.transport.write(response)

class KnockFactory(protocol.Factory):
	def buildProtocol(self, addr):
		return Knock()

reactor.listenTCP(8000, KnockFactory())
reactor.run()