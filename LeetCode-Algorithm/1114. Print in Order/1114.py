import time


class Foo:
    def __init__(self):
        self.i = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.i != 0:
            time.sleep(0.00001)

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.i += 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.i != 1:
            time.sleep(0.00001)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.i += 1

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.i != 2:
            time.sleep(0.00001)

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.i += 1


if __name__ == '__main__':
    f = Foo()
    f.third()
    f.second()
    f.first()
