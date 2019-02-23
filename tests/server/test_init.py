import signal
import socket
import threading
import time

from unittest import TestCase

from limis.server import Server


class TestServer(TestCase):
    def tearDown(self):
        try:
            if server.running:
                server.stop_server = True

                while server.running:
                    time.sleep(1)
        except NameError:
            pass

    @staticmethod
    def __listening(port):
        test_socket = socket.socket()

        try:
            test_socket.connect(('localhost', port))
        except socket.error:
            return False
        finally:
            test_socket.close()

        return True

    @staticmethod
    def __run_server():
        global server

        server = Server(None)
        server.logger.disabled = True
        server.start()

    def test_init(self):
        server = Server(None)

    def test_start_stop(self):
        thread = threading.Thread(target=TestServer.__run_server)
        thread.daemon = True
        thread.start()
        time.sleep(1)
        self.assertTrue(TestServer.__listening(server.port))
        server.stop_server = True
        while thread.is_alive():
            time.sleep(1)
        self.assertFalse(TestServer.__listening(server.port))

    def test_start_stop_with_simulated_signal(self):
        thread = threading.Thread(target=TestServer.__run_server)
        thread.daemon = True
        thread.start()
        time.sleep(1)
        self.assertTrue(TestServer.__listening(server.port))
        server._signal_handler(signal.SIGINT, None)
        while thread.is_alive():
            time.sleep(1)
        self.assertFalse(TestServer.__listening(server.port))
