import sqlite3
import csv
import datetime
import 


class PriceRecord:
    pass


class HistoryLoader:

    def __init__(self, db_file):
        self.m_dbfile = db_file

    def load(self):
        try:  # open database
            conn = sqlite3.connect(self.m_dbfile)
        except Exception:
            pass
        else:
            try:  # open  and reade from it file
                with open("EURUSD_EXPORT.csv", newline = "") as hist_file:
                    line_reader = csv.reader(hist_file, delimiter = ",")
                    row_count = 0
                    for row in line_reader:
                        # skip header
                        if row_count == 0:
                            row_count = row_count + 1
                            continue
                        else:
                            # reade the fields

                            cur = conn.cursor()

                            sql = "INSERT INTO OHLC VALUES("
                            sql = sql + "'EURUSD', 'H1', 0,"
                            sql = sql + "'" + row[0] + "', "
                            sql = sql + ",".join(row[1:5])
                            sql = sql + ", 0, '"
                            sql = sql + str(datetime.datetime.now()) + "', 1)"
                            cur.execute(sql)

            except Exception as e:
                print(e)
            finally:
                conn.commit()
                conn.close()


HL = HistoryLoader('PriceCache.db')
HL.load()








