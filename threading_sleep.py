import threading
import time

# def karra():
#   print('Men birinchi')
#   time.sleep(1)
#   print('Men ikkinchi')
# def adding():
#   print('Men uchinchi')
#   print('Men tortinchi')
# t1 = threading.Thread(target=karra, daemon=True)
# t2 = threading.Thread(target=adding)

# t1.start()
# t2.start()

import sqlite3
connection = sqlite3.connect('teschers_table.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers_table(
name TEXT,
lastname TEXT,
job TEXT
)
""")

cursor.execute("""
INSERT INTO teachers_table VALUES
('Samandar', 'Shoyimov', 'programmer'),
('Hasan', 'Husanov', 'chupon')
""")
cursor.execute("SELECT * FROM teachers_table")
print(cursor.fetchall())
