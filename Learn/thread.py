import threading

class Messenger(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = Messenger(name='send')
y = Messenger(name='receive')
x.start()
y.start()