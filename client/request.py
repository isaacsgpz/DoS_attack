from requests import get, exceptions
from threading import Thread


HOST = "localhost"
PORT = 8000

def send_requests2():
    num = 1
    while True:
        try:
            response = get(f"http://{HOST}:{PORT}/fib/{num}", timeout=None)
            if response.status_code == 200:
                print(response.text)
                num += 1
        except exceptions.RequestException as e:
            print(e)
            pass

def send_requests():
    num = 32
    while True:
        try:
            response = get(f"http://{HOST}:{PORT}/fib/{num}")
            print(response.text)
        except exceptions.RequestException:
            pass


print("Starting threads...")
for _ in range(10):
    thread = Thread(target=send_requests2)
    thread.start()
