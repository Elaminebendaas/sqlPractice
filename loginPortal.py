import sqlite3

conn = sqlite3.connect('users.db')
c = conn.execute("SELECT * FROM USERS")



#Run this once so that the TABLE which stores the users credentials is initialized
def dbInit():
    conn.execute('''
        CREATE TABLE USERS
        (USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL);''')


def accountCreation():
    creationLoop = False
    while creationLoop == False:
        print('For account creation please input a desired username of password below:\n')
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")
        checker = existanceVerification(username)
        if checker ==  True:  
            print('Username already taken, enter a new one.')
        else:
            conn.execute("INSERT INTO USERS (USERNAME,PASSWORD) VALUES(?,?)",
                (username, password))
            print("it worked?")
            creationLoop = True
        


def existanceVerification(defUsername):
    checker = False
    users = c.fetchall()
    existingUser = str(defUsername)
    for user in users:
        for elem in user:
            if elem == existingUser:
                checker = True
                return True
    if checker == False:
        return False

    





user = 'elamine'
accountCreation()
conn.commit()

users = c.fetchall()
print(users)


        


