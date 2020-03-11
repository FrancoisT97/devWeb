import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="db_ephetienn"
    )

mycursor = mydb.cursor()



def selectDb():

    sql = "Select * from user"

    mycursor.execute(sql)


    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)


def insertDb(nom, mdp):


    sql = "INSERT INTO user (name, pswd) VALUES (%s, %s)"
    val = (nom, mdp)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def updateDb():
    sql = "UPDATE user SET name = 'Canyon' WHERE id = '2'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


def deleteUser():
    sql = "DELETE FROM user WHERE id = 5"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

