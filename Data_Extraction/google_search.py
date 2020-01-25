from sys import platform
import pandas as pd
import numpy as np
import sqlite3
def data_pull() :
    if platform == "linux" or platform == "linux2":
        con = sqlite3.connect('/home/nupur/.config/google-chrome/Default/History')
        c = con.cursor()
        c.execute("SELECT url FROM urls where date(last_visit_time/1000000-11644473600,'unixepoch','localtime') = date('now')")
        results = c.fetchall()
        with open("Output/google_search.txt","w+") as out :
            for r in results :
                out.write(''.join(str(s) for s in r) + '\n')
    elif platform == "darwin":
        print("Mac")
    elif platform == "win32":
        print("Windows")
data_pull()
def data_cleaning() :
    with open('Output/google_search.txt') as f:
        content = f.readlines()

    raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]

    print(raw_data[1])
data_cleaning()
