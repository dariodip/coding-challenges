"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import threading
import time


def scheduler(f, n):

    def after_n():
        time.sleep(n/1000)
        f()

    thread = threading.Thread(target=after_n)
    thread.start()
    thread.join()


def job():
    print("Ciao")

if __name__ == "__main__":
    scheduler(job, 1000)
