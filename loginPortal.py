import sqlite3

conn = sqlite3.connect('users.db')
c = conn.execute("SELECT * FROM users")



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
        if existanceVerification(username) ==  True:  
            conn.execute("INSERT INTO USERS VALUES(?, ?)",
            (username, password))
            print('Username already taken, enter a new one.')
        else:
            print("it worked?")
            creationLoop = True
        




def existanceVerification(defUsername):
    checker = False
    users = c.fetchall()
    user = str(defUsername)
    for elem in users:
        for usa in elem:
            if usa == user:
                checker = True
                if checker == True:
                    print("System has recongized another user with the same username. Select another one")
                    return True
                else:
                    print('All clear!')
                    return False

    


    

users = c.fetchall()
user = 'elamine'
print(users)

if existanceVerification(user) == True:
    print('wtf')

        