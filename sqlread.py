import sqlite3
import time
conn = sqlite3.connect('MUD.db')
c = conn.cursor()

minval = raw_input("Min :")
maxval = raw_input("Max :")
minval = int(minval)
maxval = int(maxval)

while minval <= maxval:
    id0 = (minval,)
    c.execute('''SELECT * from ServerTime''')   # WHERE ID=?''', id0)
    fetch = c.fetchone()
    print fetch
    minval += 1
    time.sleep(1)

raw_input("End")