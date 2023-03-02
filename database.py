import mysql
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="weather"
)

global userData 
userData = ''
# create cursor
cursor = con.cursor()

# function for user login
def login(arg):
    try:
        cursor = con.cursor(dictionary=True)
        cursor.execute("select * from login where username=%s and Password=%s ", arg)
        userData = arg
        return (cursor.fetchone())


    except:
        return False



def register(arg):
    try:
        cursor.execute("INSERT INTO login (username, Password, current_location) VALUES (%s, %s, %s)", arg)
        con.commit()
        return True
    except:
        return False

def city(data1):
    print("Users City Data ", data1)
    try:
        cursor.execute("UPDATE `login` SET `city1`=%s,`city2`=%s,`city3`=%s WHERE `id`=%s ", data1)
        con.commit()
        return True
    except:
        return False


def editCity1(data):
    try:
        cursor.execute('UPDATE login SET city1 = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def editCity2(data):
    try:
        cursor.execute('UPDATE login SET city2 = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def editCity3(data):
    try:
        cursor.execute('UPDATE login SET city3 = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False