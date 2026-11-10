import numpy as np
from multiprocessing import Process, shared_memory


def worker(name, shape):

    shm = shared_memory.SharedMemory(name=name)  # gets the shared memory
    prices = np.ndarray(shape, dtype=np.float64, buffer=shm.buf)  # creates a local array, pointing tho the shared memory
    prices *= 1.01  #  writes are visible to the parent
    shm.close()  # close the local connction to shared memory


if __name__ == "__main__":
    src = np.linspace(1.08, 1.10, 5)  # creates a 5 points line of numbers between 1.08 and 110
    shm = shared_memory.SharedMemory(create=True, size=src.nbytes)  # creates a shared memory
    view = np.ndarray(src.shape, dtype=src.dtype, buffer=shm.buf)  # creates an array with the shape of the line of numbers and use the shared memory as buffer
    view[:] = src # assigns src to view
    p = Process(target=worker, args = (shm.name, src.shape)) 
    p.start()
    p.join*()

    print(view.round(5))
    shm.close()  # close the shared memory
    shm.unlink()  # unlink everything connectted to the shared memory.


