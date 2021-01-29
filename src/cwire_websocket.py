import sio as sio
import socketio


class CwireWebSocket:
    sio: socketio.Client = None

    def __init__(self, cwire):
        self.cwire = cwire
        self.sio = socketio.Client(logger=True, engineio_logger=True)

    def disconnect(self):
        if not self.sio:
            return
        self.sio.disconnect()

    def connect(self):
        self.sio.connect(
            url=self.cwire.api_url,
            headers={
                "x-access-token": self.cwire.api_key
            },
            socketio_path="/workers/sync"
        )
        print('my sid is', self.sio.sid)
        self.init_listeners()

    def on_worker_function_called(self):
        pass

    def get_worker_functions(self):
        pass

    def init_listeners(self):
        if self.sio:
            return

        @sio.on("error")
        def error(data):
            print(f"error {data}")

        @sio.on("message")
        def my_message(data):
            print('message received with ', data)

        @sio.on("CALL_WORKER_FUNCTION_ACTION")
        def call_worker_function_action():
            self.on_worker_function_called()

        @sio.on("GET_WORKER_FUNCTIONS_ACTION")
        def get_worker_function_action():
            self.get_worker_functions()
