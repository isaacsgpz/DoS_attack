from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep, time

def _fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def get_fibonacci_result(n: int) -> dict:
    start_time = time()
    return {
        'number': n,
        'fib': _fib(n),
        'time': time() - start_time,
    }

class FibonacciRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/fib/'):
            number = int(self.path.split('/')[-1])

            # result = get_fibonacci_result(number)
            result = number
            sleep(0.1)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(str(result).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not found')

def run_server():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FibonacciRequestHandler)
    print(f'Server running on {server_address}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
