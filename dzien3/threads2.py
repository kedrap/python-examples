import threading
import time


class MyWorker(threading.Thread):
    def __init__(self, delay, info):
        super().__init__()
        self.delay = delay
        self.info = info

    def run(self):
        for i in range(100):
            time.sleep(self.delay)
            print(self.info)


w1 = MyWorker(0.5, "Worker 1")
w2 = MyWorker(0.5, "Worker 2")

print(w1.is_alive())
w1.start()
print(w1.is_alive())
w2.start()
print(w1.is_alive())

print("in main thread")

w1.join()
w2.join()
