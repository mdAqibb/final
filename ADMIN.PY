import SQLFUNC
def addnewres():
    resortname = input("Enter resort name")
    location = input("Enter city")
    price = input("Enter Price per night")
    descrip = input("Describe the resort")
    facility = input("Faiclities available")
    SQLFUNC.mycur.execute("use resorts")
    query = "Insert into resorts values('{}','{}',{},'{}','{}',{})".format(resortname, location, price, descrip,
                                                                           facility, 4)
    SQLFUNC.mycur.execute(query)
    SQLFUNC.mycon.commit()


def seeall():
    query="select*from resorts"
    SQLFUNC.mycur.execute(query)
    data= SQLFUNC.mycur.fetchall()
    print(data)
