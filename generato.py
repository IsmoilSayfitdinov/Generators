class Range:
    def __init__(self, start: int, stop: int = None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step
        else:
            self.start = start - step
            self.stop = stop
            self.step =  step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop and self.step > 0:
            self.start += self.step
            raise StopIteration
        if self.start > self.stop and self.step < 0:
            self.start += self.step
            raise StopIteration



for i in Range(start, stop, step):
    print(i)



def task1():
    a = [1, 4, 6, 2, 6, 2]
    for i in a:
        i = i
        print(i)
        return i
def task2():
    return 4 ** 4
def task3():
    return 4 + 3

def main():
    yield task1()
    yield task2()
    yield task3()

if __name__ == '__main__':
    for i in main():
        print(i)