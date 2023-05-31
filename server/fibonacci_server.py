import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable
from urllib.parse import urlparse, parse_qs
from time import sleep

class FibonacciServer(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self._routes = {
            '/': self.handle_home,
            '/fib': self.handle_fib,
        }
        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            params = {key: query_params.get(key, [None])[0] for key in query_params}

            if self.path.split('?')[0] in self._routes:
                handler_method: Callable = self._routes[self.path.split('?')[0]]
                handler_method(**params)
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def handle_home(self, **params):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

    def handle_fib(self, **params):
        number_str = params.get('number', '0')

        try:
            number = int(number_str)
        except ValueError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {
                'error': 'Invalid parameter',
                'message': f'Invalid value for parameter "number": {number_str}',
            }
            self.wfile.write(json.dumps(error_response).encode())
            return

        response = {
            'number': number,
            'fib': self._calculate_fibonacci(number),
        }

        sleep(0.1)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def _calculate_fibonacci(self, n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


def run_server():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FibonacciServer)
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
