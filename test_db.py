import sqlite3

conn = sqlite3.connect('dati.db')
c = conn.cursor()

# Pārbaudi, vai tabula satur ierakstus
c.execute("SELECT * FROM rezultati")
rezultati = c.fetchall()
print("Datubāzes ieraksti:", rezultati)

conn.close()
