import sqlite3 as sql

db = sql.connect("Db")            
cursor = db.cursor()
        
def tabloOlustur(tabloAdi,kolonAd,kolonAd2):
    cursor.execute(f"Create table {tabloAdi} ({kolonAd},{kolonAd2})")
    db.commit()

def tabloSil(tabloAdi):
    cursor.execute(f"Drop table {tabloAdi}")
    print("Tablo silindi !")

def Verigir(tabloAdi,isim,soyisim):
        sorgu = f"""  insert into {tabloAdi} values(?,?) """
        cursor.execute(sorgu,(isim,soyisim))
        db.commit()    
    
def Listele(tabloAdi):
    cursor.execute(f"Select * from {tabloAdi}")
    veriler = cursor.fetchall()
    print("Geriye değer olarak donduruldu")
    return veriler
