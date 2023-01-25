import SQLFUNC

def NewUser():
        username = input("enter new user name: ")
        first_name = input("enter first name: ")
        last_name = input("enter last name: ")
        password = input("enter password: ")


def LogInUser():
        username=input("enter username: ")
        password=input("enter password: ")
        a = "select * from database where username = '{}' and password = '{}'".format(username.password)
        SQLFUNC.mycur.execute(a)


def LogInAdmin():
        passwords='royalflake'
        password=input("enter password: ")
        if password == passwords :
                print("Access Granted")
        else:
                print("Access Denied")



