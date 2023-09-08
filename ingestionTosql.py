import mysql.connector
import pandas as pd

import csv
   
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "Matkhaumanh1", database = "car_showroom")
 
# in đối tượng connection ra màn hình
print(myconn)
 
# tạo đối tượng cursor
cur = myconn.cursor()
sql = ("insert into car(name,yom, price, origin, status, KMtraveled, color, doorNumber,seatNumber, engine, Comsumption) "
    "values (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s )")

with open('./car/allcar.csv', newline='', encoding="utf8") as csvfile:
    data = list(csv.reader(csvfile))
    for row in data:
        cur.execute(sql, (row))
        myconn.commit()
        
print("record inserted!")
myconn.close()