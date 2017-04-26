import random
import time


from threading import Thread


class MyThread(Thread):
    """
    A threading example
    """
    def __init__(self, name):
        """initialize the thread"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """run the thread"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)


def create_threads():
    """create a group of threads"""
    for i in range(5):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == '__main__':
    create_threads()