import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
from termcolor import colored


class FibonacciRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.status = 200

        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            if self.path == "/":
                self._handle_home()
            elif self.path.startswith("/fib"):
                self._handle_fib(self.path.split("/")[2])
            else:
                return self._send_response(404)
        except Exception:
            return self._send_response(500)
        finally:
            sleep(0.1)

    def log_message(self, format, *args):
        color = "red" if self.status >= 400 else "green"
        host = self.headers.get("Host", "localhost")
        print(
            f'{colored(self.command, color, attrs=["bold"])}/'
            f'{colored(self.status, color, attrs=["bold"])} => '
            f'{colored(f"http://{host}{self.path}", "white")}'
        )

    def _send_response(self, status: int, content_type: str = "application/json"):
        self.status = status
        if status >= 400:
            return self.send_error(status)

        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def _handle_home(self):
        html = os.path.join(self.root_dir, "public", "index.html")
        self._send_response(200, "text/html")

        with open(html, "r") as file:
            html_content = file.read()
        self.wfile.write(html_content.encode())

    def _handle_fib(self, number_str: str):
        try:
            number = int(number_str)
        except ValueError:
            return self._send_response(400)

        response = {
            "number": number,
            "fib": self._calculate_fibonacci(number),
        }

        self._send_response(200)
        self.wfile.write(json.dumps(response).encode())
        return

    def _calculate_fibonacci(self, n: int):
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y
        return x


class FibonacciServer:
    def __init__(self, host="localhost", port=8000):
        self.host = host
        self.port = port
        self.server: HTTPServer = None

    def start(self):
        print(colored(f"Server started at http://{self.host}:{self.port}", "yellow"))
        self.server = HTTPServer((self.host, self.port), FibonacciRequestHandler)
        self.server.serve_forever()

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print(colored("\nServer stopped", "yellow"))
