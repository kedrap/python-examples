class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __next__(self):
        if self.limit > 0:
            self.limit -= 1
            return self.limit
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def down(self):
        for x in range(self.limit, 0, -1):
            print(x)


cd = Counter(10)
#cd.down()

cd = list(Counter(10))
print(cd)
