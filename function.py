import database
import sqlite3 as sql

db = database.db
cursor = database.cursor

database.tabloOlustur("kisi","ad","soyad")
database.tabloSil("kisi")
database.Verigir("kisi","berat","erdinc")
database.Listele("kisi")
