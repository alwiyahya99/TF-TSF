import time
import pymysql

data = input('Masukan Data : ')
d = data.split(',')
con = pymysql.connect( db="raspberry",
                       user="root",
                       passwd="",
                       host="localhost",
                       port = 3306)
cursor = con.cursor()
sql = "INSERT INTO gateway (no1,no2) VALUES (%s,%s)"

val1 = [(d[1],d[2])]

while True:
    #print data
    print (val1)
    cursor.executemany(sql, val1)
    con.commit()
    time.sleep(1)