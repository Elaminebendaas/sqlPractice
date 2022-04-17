import sqlite3



def dbInit():
    conn.execute('''
        CREATE TABLE USERS
        (USERID INT PRIMARY KEY,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL);''')


def accountCreation():
    print('For account creation please input a desired username of password below:\n')
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")
    conn.execute("INSERT INTO USERS (%s, %s)", (username, password))
    users = c.fetchall()
    print(users)




conn = sqlite3.connect('users.db')
c = conn.execute("SELECT * FROM users")


accountCreation()


