import sqlite3
conn = sqlite3.connect('MUD.db')
c = conn.cursor()
minval = 1
maxval = 30
while minval <= maxval:
    id0 = (minval,)
    c.execute('''SELECT * from RoomPlayers WHERE ID=?''', id0)
    fetch = c.fetchone()
    print fetch
    minval += 1

raw_input("End")