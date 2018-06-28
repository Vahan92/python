import threading
import os

def task1():
    for i in range(0, 100):
        print "task-1" 
    #print("Task 1 assigned to thread: {} ".format(threading.current_thread().name))
    #print("ID of process running task 1: {}".format(os.getpid()))

def task3():
    for i in range(0, 100):
        print "task-3"


def task2():
    for i in range(0, 100):
        print "task-2"
    t3 = threading.Thread(target=task3, name='t3')
    t3.start()
    t3.join()
    #print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    #print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":
    for i in range(0, 100):
        print "YeYe"
    #print ID of current process
    #print("ID of process running main program: {}".format(os.getpid()))

    #print name of main thread
    #print("Main thread name: {}".format(threading.main_thread().name))

    #creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2') 

    #starting threads
    t1.start()
    t2.start()

    #wait until all threads finish
    t1.join()
    t2.join()
