from ..objs.game_object import GameObject
from ..objs.car import Car
import select

SEPARATOR = "\x00"

"""
Thanks to https://github.com/anacrolix/archive/blob/master/projects/pimu/common.py
Very useful stuff :)
"""

Message = collections.namedtuple("Message", ("title", "args", "kwargs"))

class SocketClosed(Exception):
	pass

class InvalidMessage(Exception):
	pass

class SocketMessageBuffer:
    def __init__(self, socket):
        self.incoming = ""
        self.outgoing = ""
        self.socket = socket
    
    def get_socket(self):
        return self.socket
    
    def send(self, title, *args, **kwargs):
        self.outgoing += repr((title, args, kwargs)) + SEPARATOR

    def receive(self):
        try:
            index = self.incoming.index(SEPARATOR)
        except ValueError:
            return
        
        data = self.incoming[:index]
        self.incoming = self.incoming[index + 1:]

        try:
            return Message(*eval(data))
        except SyntaxError as e:
            raise InvalidMessage(repr(e.text))

    def flush(self):
        if self.pending_out():
			write_fds = [self.socket]
		else:
			write_fds = []

		ready = select.select([self.socket], write_fds, [], 0)
		
        if ready[0] and not self.receive_more():
			return False

		if ready[1]:
			self.send_pending()

		return True

	def send_pending(self):
		assert len(self.outgoing) > 0

		sent = self.socket.send(self.outgoing)
		assert sent != 0

		self.outgoing = self.outgoing[sent:]

	def receive_more(self):
		data = self.socket.recv(0x1000)

		if not data:
			raise SocketClosed()

		self.incoming += data
		return len(data) > 0

	def pending_out(self):
		return len(self.outgoing) > 0

	def fileno(self):
		return self.socket.fileno()

class Server:

    def __init__(self, addr=("", 8080)):
        self.socket = socket.create_server(addr)
        self.client_sockets = []

    def accept_connection(self, conn):
        pass