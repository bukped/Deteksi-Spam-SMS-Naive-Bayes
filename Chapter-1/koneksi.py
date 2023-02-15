import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="buku_py_zaky"
)

if db.is_connected():
  print("Berhasil terhubung ke database")