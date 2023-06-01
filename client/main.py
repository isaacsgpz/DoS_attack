from threading import Thread

from requests import exceptions, get

HOST = "localhost"
PORT = 8000


class Client(Thread):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        super().__init__()

    def run(self):
        num = 1
        while True:
            try:
                response = get(
                    f"http://{self.host}:{self.port}/fib",
                    params={"number": num},
                    timeout=None,
                )
                if response.status_code == 200:
                    print(response.text)
                    num += 1
            except (exceptions.RequestException, Exception):
                pass


class DoS:
    def __init__(self, host="localhost", port=8000):
        self.host = host
        self.port = port

    def start(self, num_threads=10):
        print("Starting threads...")
        for _ in range(num_threads):
            thread = Client(self.host, self.port)
            thread.start()


if __name__ == "__main__":
    dos = DoS(HOST, PORT)
    dos.start()

# python3 client/main.py
