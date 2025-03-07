import threading
import time


def print_numbers(name):
    for i in range(1, 6):
        print(f"{name}: {i}")
        time.sleep(1)


def print_10_numbers(name):
    for i in range(1, 11):
        print(f"{name}: {i}")
        time.sleep(1)


thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
thread2 = threading.Thread(target=print_10_numbers, args=("Thread-2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished.")
