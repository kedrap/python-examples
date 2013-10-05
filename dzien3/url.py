import threading
import urllib.request
import time

start = time.time()
lock = threading.Lock()

urls = [
    "http://interia.pl",
    "http://wp.pl",
    "http://gazeta.pl",
    "http://ibm.pl",
    "http://yahoo.pl",
]


class MyWorker(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        u = urllib.request.urlopen(self.url)
        buff = u.read()
        with lock:
            #lock.acquire()
            #try:
            print(self.url, ":", len(buff))
            import random

            if random.choice(range(5)) == 2:
                #raise KeyError
                pass
                #finally:
                #    pass
                #lock.release()


workers = []
for url in urls:
    workers.append(MyWorker(url))
    workers[-1].start()

print("time 1: ", round(time.time() - start, 2), " s")

for worker in workers:
    worker.join()
    #pass

print("time 2: ", round(time.time() - start, 2), " s")
9