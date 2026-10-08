# TODO: Read a large pandas sequentially and using threads and compare times.

import time
from threading import Thread

import pandas as pd


FILE_PATH:str = "/home/mchiuminatto/work/dev/tradig-strategy-research/data/raw/"
FILE_1: str = "USDCHF_4 Hours_Ask_2014.08.31_2026.09.01.parquet"
FILE_2: str = "USDCHF_4 Hours_Bid_2014.08.31_2026.09.01.parquet"


def read_file(file_name: str) -> pd.DataFrame:
    return pd.read_parquet(f"{file_name}")
    
# --------------- sequenctial reading -------------------------
print("------- sequential reading ---------")
w0 = time.perf_counter()
c0 = time.process_time()

df_1 = read_file(f"{FILE_PATH}{FILE_1}")
df_2 = read_file(f"{FILE_PATH}{FILE_2}")


wall_time = time.perf_counter() - w0
cpu_time = time.process_time() - c0

print(f"Wall time = {wall_time : .4f} ")
print(f"CPU time = {cpu_time : .4f}")

# ----------------- threaded reading ----------------------------

print("------- multithread reading ---------")

files_to_process = [f"{FILE_PATH}{FILE_1}", f"{FILE_PATH}{FILE_2}"]
COLLECTOR_CONTAINER: dict = {}


def read_file_to_container(file_name: str) -> pd.DataFrame:
    COLLECTOR_CONTAINER[file_name]  = pd.read_parquet(f"{file_name}")

w0 = time.perf_counter()
c0 = time.process_time()


threads = [Thread(target=read_file_to_container, args=(file,)) for file in files_to_process]
for thread in threads: 
    thread.start()

for thread in threads: 
    thread.join()

wall_time = time.perf_counter() - w0
cpu_time = time.process_time() - c0


print(f"Wall time = {wall_time : .4f} ")
print(f"CPU time = {cpu_time : .4f}")


FEATURE_CONTANIER: dict = {}

def process_file(dataset: pd.DataFrame) -> pd.DataFrame:

    features: list = []
    features_names: list = []
    for i in range(10, 50000, 50):

        dataset[f"mva_{i}"] = dataset["close"].rolling(i).mean()
    return dataset

# ------------ process in sequence --------

print("-------------------- process files sequentially -------------------")
w0 = time.perf_counter()
c0 = time.process_time()

df1 = process_file(COLLECTOR_CONTAINER[files_to_process[0]])
df2 = process_file(COLLECTOR_CONTAINER[files_to_process[1]])

wall_time = time.perf_counter() - w0
cpu_time = time.process_time() - c0

print(f"Wall time = {wall_time : .4f} ")
print(f"CPU time = {cpu_time : .4f}")


# ------------------------ Process files in threads -------------------
print("-------------------- process files threaded -------------------")
w0 = time.perf_counter()
c0 = time.process_time()

threads = [Thread(target=process_file, args=(file, ))
                   for file in COLLECTOR_CONTAINER.values()]


wall_time = time.perf_counter() - w0
cpu_time = time.process_time() - c0

for thread in threads: 
    thread.start()


for thread in threads: 
    thread.join()


print(f"Wall time = {wall_time : .5f} ")
print(f"CPU time = {cpu_time : .5f}")
