from fibonacci_server import FibonacciServer
from termcolor import colored

HOST = "localhost"
PORT = 8000


def run_server():
    try:
        server = FibonacciServer(HOST, PORT)
        server.start()
    except KeyboardInterrupt:
        server.stop()
        print(colored("Exiting...", "yellow"))


if __name__ == "__main__":
    run_server()

# python3 server/fibonacci_server.py
