import mysql.connector as mysql
mycon=mysql.connect(
        host="localhost",
        user="root",
        password="abiyaaqib"
)
if (not mycon.is_connected()):
         print("connection to database not established")

mycur = mycon.cursor()

def closeDB():
    mycon.close()