from datetime import datetime
import time

with open('workfile.txt', "w") as f:
	read_data = f.write(datetime.today().__str__())
	time.sleep(5)
	