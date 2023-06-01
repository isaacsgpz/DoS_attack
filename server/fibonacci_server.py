import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
from typing import Callable
from urllib.parse import parse_qs, urlparse

from termcolor import colored


class FibonacciRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self._routes = {
            "/": self._handle_home,
            "/fib": self._handle_fib,
        }

        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            self.parsed_url = urlparse(self.path)
            query_params = parse_qs(self.parsed_url.query)
            params = {key: query_params.get(key, [None])[0] for key in query_params}

            if self.path.split("?")[0] in self._routes:
                handler_method: Callable = self._routes[self.path.split("?")[0]]
                handler_method(**params)
            else:
                self._send_response_headers(404)
                return
        except Exception:
            self._send_response_headers(500)
            return
        finally:
            sleep(0.1)

    def log_message(self, format, *args):
        pass

    def _print_request_info(self, endpoint: str, status: int):
        print_color = "red" if status >= 400 else "green"
        url = f"http://localhost{self.path}" or f"http://localhost{endpoint}"
        print(
            f'{colored(self.command, print_color, attrs=["bold"])}/{colored(status, print_color, attrs=["bold"])} => {colored(url, "white")}'
        )

    def _send_response_headers(
        self, status: int, content_type: str = "application/json"
    ):
        self._print_request_info(self.parsed_url.path, status)
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    # Route handlers ==============================================
    def _handle_home(self, **params):
        html_file_path = os.path.join(self.current_dir, "public", "index.html")
        self._send_response_headers(200, "text/html")

        with open(html_file_path, "r") as file:
            html_content = file.read()
        self.wfile.write(html_content.encode())

    def _handle_fib(self, **params):
        number_str = params.get("number", "0")
        try:
            number = int(number_str)
        except ValueError:
            self._send_response_headers(400)
            return

        response = {
            "number": number,
            "fib": self._calculate_fibonacci(number),
        }

        self._send_response_headers(200)
        self.wfile.write(json.dumps(response).encode())

    def _calculate_fibonacci(self, n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


class FibonacciServer:
    def __init__(self, host="localhost", port=8000):
        self.host = host
        self.port = port
        self.server: HTTPServer = None

    print(os.curdir)

    def start(self):
        print(colored(f"Server started at http://{self.host}:{self.port}", "yellow"))
        self.server = HTTPServer((self.host, self.port), FibonacciRequestHandler)
        self.server.serve_forever()

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print(colored("\nServer stopped", "yellow"))
