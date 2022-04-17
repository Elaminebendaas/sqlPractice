import sqlite3

#CREATES/CONNECTS TO DATABSE *STILL REQUIRED TO CREATE TABLES TO STORE DATA*
conn = sqlite3.connect('test.db')


#THIS ALLOWS YOU TO SELECT CERTAIN ASPECTS FOR CREATED TABLE IN THE DATABASE
c = conn.execute("SELECT id, username, password from USERS")
#OR
#c = conn.execute("SELECT * FROM users")


#THIS CREATES A TABLE IN THE DATABASE SELECTED (conn)
#conn.execute('''CREATE TABLE USERS
       # (ID INT PRIMARY KEY NOT NULL,
       # USERNAME TEXT NOT NULL,
       # PASSWORD TEXT NOT NULL);''')



#THIS IS FOR INSERTING VALUES IN A DATABASE
#conn.execute("INSERT INTO USERS (ID,USERNAME,PASSWORD)  VALUES (1 , 'hello1','npc1')") 
#conn.execute("INSERT INTO USERS (ID,USERNAME,PASSWORD)  VALUES (2 , 'hello2','npc2')")
#conn.execute("INSERT INTO USERS (ID,USERNAME,PASSWORD)  VALUES (3 , 'hello3','npc3')")






#FETCHES THE WHOLE TABLE THAT THE CURSOR IS ON
users = c.fetchall()

c.execute("SELECT * FROM users WHERE username = 'hello'")






for user in users:
    print(user)
  
conn.commit()