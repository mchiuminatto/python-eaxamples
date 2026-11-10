import multiprocessing as mp

STOP = None

def parser(inbox: mp.Queue, outbox: mp.Queue):
    while (line:=inbox.get()) is not STOP:  # iterates on the input queue
        pair, bid, ask = line.split(", ")
        spread = round((float(ask) - float(bid))*1e4, 1)
        outbox.put((pair, spread))  # put the parsed values into the output queue
    outbox.put(STOP)  # put the STOP in the outbox queue to signal work done.


if __name__ == "__main__":
        lines = [
             "EURUSD, 1.0850, 1.0851", 
             "GBPUSD, 1.2700, 1.2702",
             "USDCHF, 0.8800, 0.8802", 
             "AUDUSD, 0.6600, 0.6601"
             ]
        inbox, outbox = mp.Queue(), mp.Queue()  # creates inbox/outbox queue

        # prepare the worker list
        workers = [mp.Process(target=parser, args=(inbox, outbox)) for _ in range(2)]

        for w in workers: w.start()  # launch the workers
        for line in lines: inbox.put(line)  # put the lines in the input queue
        for _ in workers: inbox.put(STOP)  # send the stop for each worker

        finished = 0  # control counter: holds the finished workers
        spreads = {}   # for collecting the results.

        while finished < len(workers):  # while not all workeres are finished
            item = outbox.get()  # pull item from the outbox
            if item is STOP:  # if the item is a stop, incres the control counter
                finished += 1
            else:  # not a stop, collects results
                print(item)
                spreads[item[0]] = item[1]

        for w in workers: w.join()  # finally joun the workers

        print(dict(sorted(spreads.items())))


