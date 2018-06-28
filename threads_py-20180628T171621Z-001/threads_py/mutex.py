import threading
import os, time

my_mutex = threading.Lock()

def task1():
    global my_mutex
    for i in range(0, 100):
        print "task-1"
    time.sleep(9) 
    my_mutex.release()
    #print("Task 1 assigned to thread: {} ".format(threading.current_thread().name))
    #print("ID of process running task 1: {}".format(os.getpid()))

def task3():
    global my_mutex
    for i in range(0, 100):
        print "task-3"
    time.sleep(9) 
    my_mutex.acquire() 

def task2():
    global my_mutex
    for i in range(0, 100):
        print "task-2"
    time.sleep(9) 
    my_mutex.release()
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
    my_mutex.acquire() 
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2') 

    #starting threads
    t1.start()
    t2.start()

    #wait until all threads finish
    t1.join()
    t2.join()
