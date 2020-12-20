import socketio

from src.cwire import Cwire


class CwireWebSocket:
    socket: socketio.AsyncClient = None

    def __init__(self, cwire: Cwire):
        self.cwire = cwire

    def disconnect(self):
        if self.socket:
            return

        self.socket.disconnect()

    def connect(self):
        self.socket = socketio.AsyncClient().connect(
            url=self.cwire.api_url,

        )