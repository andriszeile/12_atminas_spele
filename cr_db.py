import sqlite3

# Izveido savienojumu ar datubāzi (ja faili nepastāv, tie tiks izveidoti)
conn = sqlite3.connect('dati.db')
c = conn.cursor()

# Izveido tabulu rezultātiem
c.execute('''
CREATE TABLE IF NOT EXISTS rezultati (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    klikski INTEGER NOT NULL,
    laiks INTEGER NOT NULL,
    datums TEXT NOT NULL
)
''')

# Piecu izdomātu ierakstu saraksts
ieraksti = [
    ("Jānis", 34, 50, "2025-01-20"),
    ("Anna", 28, 45, "2025-01-21"),
    ("Pēteris", 40, 60, "2025-01-22"),
    ("Zane", 30, 55, "2025-01-23"),
    ("Ilze", 25, 40, "2025-01-24"),
]

# Pievieno ierakstus tabulā
c.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
VALUES (?, ?, ?, ?)
''', ieraksti)

# Saglabā izmaiņas un aizver savienojumu
conn.commit()
conn.close()

print("Datubāze un ieraksti veiksmīgi izveidoti!")
