import mysql.connector

# Konfigurasi koneksi ke MariaDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Ganti jika ada password
    database="contoh_db"
)

# Buat cursor untuk eksekusi query
cursor = conn.cursor()

# Query untuk mengambil data dari tabel
cursor.execute("SELECT * FROM pengguna")

# Ambil semua hasil query
results = cursor.fetchall()

# Tampilkan hasil
print("Daftar Pengguna:")
for row in results:import mysql.connector
from mysql.connector import Error

# Konfigurasi koneksi ke MariaDB
def connect_to_db(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Buat cursor untuk eksekusi query
def create_cursor(conn):
    try:
        cursor = conn.cursor()
        return cursor
    except Error as e:
        print(f"Error creating cursor: {e}")
        return None

# Query untuk mengambil data dari tabel
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Error executing query: {e}")
        return None

# Tampilkan hasil
def print_results(results):
    if results is not None:
        print("Daftar Pengguna:")
        for row in results:
            print(f"ID: {row[0]}, Nama: {row[1]}, Email: {row[2]}")
    else:
        print("No results found.")

# Tutup koneksi
def close_connection(conn, cursor):
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()

# Main program
if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = ""  # Ganti jika ada password
    database = "contoh_db"
    query = "SELECT * FROM pengguna"

    conn = connect_to_db(host, user, password, database)
    if conn is not None:
        cursor = create_cursor(conn)
        if cursor is not None:
            results = execute_query(cursor, query)
            print_results(results)
            close_connection(conn, cursor)
    print(f"ID: {row[0]}, Nama: {row[1]}, Email: {row[2]}")

# Tutup koneksi
cursor.close()
conn.close()
