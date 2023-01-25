from resorts import SQLFUNC


def searchby(city):
    query="select*from resorts where location="+city
    SQLFUNC.mycur.execute("use resorts")
    SQLFUNC.mycur.execute(query)

def sortbyprice():
    SQLFUNC.mycur.execute("use resorts")
    SQLFUNC.mycur.execute("Select * from resorts order by price")
    print(SQLFUNC.mycur.fetchall())

def sortbyrating():
    SQLFUNC.mycur.execute("use resorts")
    SQLFUNC.mycur.execute("Select * from resorts order by rating")
    print(SQLFUNC.mycur.fetchall())

def seebookingsbyself(username):
    SQLFUNC.mycur.execute("use bookings")
    SQLFUNC.mycur.execute("Select * from bookings where username =", username)#username to be taken from members page
    print(SQLFUNC.mycur.fetchall())

def modifydate(resortgoingto):
    resname=input("enter resort to be editted")
    start=input("new arrival at resort (in DD-MM-YYYY format)")
    end=input("new date of departure (in DD-MM-YYYY format)")
    #s=cursor.execute("select start_date from bookings")
    #e=cursor.execute("selec end_date from bookings")

    SQLFUNC.mycur.execute("use resorts")
    SQLFUNC.mycur.execute("update bookings set start_date=", start, "and end_date=", end, "where resort_name=", resname)
    print(SQLFUNC.mycur.fetchall())