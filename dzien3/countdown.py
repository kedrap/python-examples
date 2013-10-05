class Countdown:
    def __init__(self, limit):
        self.limit = limit

    def __next__(self):
        self.limit -= 1
        if self.limit < 0:
            raise StopIteration
        else:
            return self.limit

    def __iter__(self):
        return self

# wywolania
# ist(Countdown(10))
#
# c = Countdown(10)
# c.__next__()
# c.__next__()
