import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    database="ecommerce",
    user="root",
    password=""
)

cursor = db.cursor()

cursor.execute("DESCRIBE kategoripenjual")
result = cursor.fetchall()
print("Struktur tabel kategoripenjual:")
for column in result:
    print(column)

cursor.execute("SELECT * FROM kategoripenjual LIMIT 5")
data = cursor.fetchall()
print("\nData dalam tabel kategoripenjual:")
for row in data:
    print(row)

cursor.close()
db.close() 