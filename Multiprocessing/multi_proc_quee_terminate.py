from multiprocessing import Process, Queue


def f(q):
        while True:
            element = q.get()
            print("read from queue", element)


if __name__ == '__main__':
    q = Queue() # creates a queue to communicate process
    p = Process(target=f, args=(q,))    # spawn the function f, with queue as arg
    p.start()  # statrts the process
    while True:
        var = input("Please enter something: ")  # process user input
        print("Queue", var)  # prints the value
        q.put(var)  # queues the value
        if (var == "exit"):  # in case the input value is exit ends the process
            #p.join()  # rejoins the process flows
            p.terminate()   # terminate the spawned process
            break  # ends the  while



