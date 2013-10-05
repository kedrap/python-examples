import threading
import time


def worker(delay, info):
    for i in range(10):
        time.sleep(delay)
        print(info)


w1 = threading.Thread(target=worker, args=(0.5, "Worker 1"))
w2 = threading.Thread(target=worker, args=(0.5, "Worker 2"))

w1.start()
w2.start()

print("in main thread")

w1.join()
w2.join()
