from collections import deque

# initialize de queues
Date = deque()
Time = deque()
Open = deque()
High = deque()
Low  = deque()
Close = deque()
PRECISION = 4


def batch_mva(n):
    """
    Caluclate n periods mva for an OHLC file
    
    
    :param n: 
    :return: nil
    """
    # OPEN INPUT FILE

    # creates a file object from file ohlc.csv modes can be used
    # r: read (default), w: write, a:append, r+: read/write
    # ba appended to previous modes will open the file in binary mode

    fi = open("ohlc.csv")
    fi.readline()  # read and discard header

    fo = open("mva.csv", "w")

    # write output file headers
    h = "DATE, TIME, MVA_OPEN, MVA_HIGH, MVA_LOW, MVA_CLOSE\n"
    fo.write(h)

    # iterate, calculate and write
    count_l = 0
    for line in fi:
        count_l = count_l + 1
        # add line values to respective queues
        queue_value(line)
        if count_l >= n:  # starts calculating mva when have added n records to the queues
            # extracts and calculates values
            col_date = Date[-1]
            col_time = Time[-1]
            mva_open = round(calc_mva(Open), PRECISION)
            mva_high = round(calc_mva(High), PRECISION)
            mva_low = round(calc_mva(Low), PRECISION)
            mva_close = round(calc_mva(Close), PRECISION)

            # write to file
            r = str(col_date)
            r = r + "," + str(col_time)
            r = r + "," + str(mva_open)
            r = r + "," + str(mva_high)
            r = r + "," + str(mva_low)
            r = r + "," + str(mva_close)

            fo.write(r + "\n")

            # pop from the left all values
            Date.popleft()
            Time.popleft()
            Open.popleft()
            High.popleft()
            Low.popleft()
            Close.popleft()

    fi.close()
    fo.close()


def queue_value(line):
    """
    fill the global queues
    
    split a OHLC csv line and adds values to to the 
    global queues Date, Time, Open, High, Low and Close
    
    :param line: 
    :return: 
    """
    val_list = line.split(",")
    Date.append(val_list[0])  # first index on lists is 0
    Time.append(val_list[1])
    Open.append(float(val_list[3]))
    High.append(float(val_list[4]))
    Low.append(float(val_list[5]))
    Close.append(float(val_list[6]))


def calc_mva(q):
    """
    calculates mva for a collection
    
    it calculates mva fot all the values that the collection q
    contains
    :param q: 
    :return: mva
    """

    acc = 0
    count = 0
    mva = 0
    for v in q:
        acc = acc + v
        count = count + 1
    if count != 0:
        mva = acc/count

    return mva

# execute function
batch_mva(10)
