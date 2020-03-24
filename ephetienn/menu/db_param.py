import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="db_ephetienn"
)

mycursor = mydb.cursor()


def afficherInfoDb(nomDb):
    sql = ("Select * from {0}").format(nomDb)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


def insertUser(nom, mdp):
    sql = "INSERT INTO user (name, pswd) VALUES (%s, %s)"
    val = (nom, mdp)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    
def insertEvent(date, event, description):
    sql = ("INSERT INTO event (dateEvent, nameEvent, descEvent) VALUES ('{0}', '{1}', '{2}')").format(date, event, description)
    # date au format '2020-03-11'


    print(sql)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def insertInscription(nom, prenom, dateNaiss, numTel, emailParent, remarques):
    sql = ("INSERT INTO inscrits (nom, prenom, dateNaiss, numTel, emailParent, remarques) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')").format(nom, prenom,dateNaiss, numTel, emailParent, remarques)
    # date au format '2020-03-11'

    print(sql)
    mycursor.execute(sql)

    mydb.commit()






def updateUser(id):
    sql = ("UPDATE user SET name = 'Canyon' WHERE id = {0}").format(id)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


def deleteData(nomDb, id):
    sql = ("DELETE FROM {0} WHERE id = {1}").format(nomDb, id)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")



