import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="ephetienne"
)

mycursor = mydb.cursor()


def afficherInfoDb(nomDb):
    element = []
    sql = ("Select * from {0}").format(nomDb)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        element = myresult


    return element


def insertUser(nom, mdp):
    sql = "INSERT INTO user (userName, userPswd) VALUES (%s, %s)"
    val = (nom, mdp)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    
def insertEvent(event, date, description):
    sql = ("INSERT INTO event (eventName, eventDate, eventDesc) VALUES ('{0}', '{1}', '{2}')").format(date, event, description)
    # date au format '2020-03-11'


    print(sql)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def insertInscription(nom, prenom, dateNaiss, numTel, emailParent, remarques):
    sql = ("INSERT INTO membre (membreNom, membrePrenom, dateNaiss, telParent, emailParent, remarques) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')").format(nom, prenom, dateNaiss, numTel, emailParent, remarques)
    # date au format '2020-03-11'

    print(sql)
    mycursor.execute(sql)

    mydb.commit()




def updateUser(id):
    sql = ("UPDATE user SET name = 'Canyon' WHERE id = {0}").format(id)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


def deleteMembre(id):
    sql = ("DELETE FROM membre WHERE idmembre = {0}").format(id)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def selectUser(user, mdp):
    sql = ("Select * from user")

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[1], x[2])
        if user == x[1] and mdp == x[2]:
            return True

def modifMembreDb(id):
    sql = ("Select * from membre where idmembre = {0}").format(id)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    #debug
    print(myresult)

    #debug
    print(sql)

    return myresult

def supEventDb(nom, date):

  sql = ("Delete from event Where eventName = '{0}' and eventDate = '{1}' ").format(nom, date)
  mycursor.execute(sql)
  print(sql)

  mydb.commit()

  print("effacement réussi")


def selectMembre(id):
    sql = ("Select * from membre where idmembre = {0}").format(id)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    # debug
    print(myresult)

    # debug
    print(sql)

    return myresult

def updateMembre(id, nom, prenom, dateNaiss, numTel, email, rem):
    sql = ("UPDATE membre set membreNom = '{1}', membrePrenom = '{2}', dateNaiss= '{3}', telParent = '{4}', emailParent = '{5}', remarques = '{6}'  where idmembre = {0}").format(id, nom, prenom, dateNaiss, numTel, email, rem)

    print(sql)
    mycursor.execute(sql)

    mydb.commit()





