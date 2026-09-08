import threading

class MyThread(threading.Thread):

    def task(self):
        for i in range(5):
            print("Thread is running")

    def run(self):
        self.task()

    def task2(self):
        for i in range(3):
            print("Thread is running")

t1 = MyThread()
t2 = MyThread()
t1.start()
t1.join()
t2.start()
t2.join()

print("Thread has completed its task")