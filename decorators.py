import datetime
import time

def timer(func):
    def wrapper():
        print("Entered Timer wrapper")
        start = datetime.datetime.now()
        func()
        endtime = datetime.datetime.now() - start
        print("Time taken for execution of {}".format(endtime))
    return wrapper

def handshake(func):
    def wrapper():
        try:
            func()
        except:
            print("Execution Result failure")
    return wrapper

@timer
@handshake
def exec_function():
    print("About to sleep")
    time.sleep(5)
    print("Waking up after 5")

def main():
    exec_function()

if __name__ == '__main__':
    main()
