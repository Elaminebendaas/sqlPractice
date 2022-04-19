import sqlite3

db = sqlite3.connect('practice.db')
c = db.execute("SELECT * FROM users")
password = "lmao123"

#db.execute('''CREATE TABLE USERS
		#(USERNAME TEXT NOT NULL,
		#PASSWORD TEXT NOT NULL);''')


randomUsernames = ['mahand1','mahand2','elamino','elamine',
				'paserie','elias','rub','yeetah','admo',
				'ilyas','elaminio','mouad','ben','ethan',
				'mina','adam','elliot','tiany','adnan']

for user in randomUsernames:
	print(user)
	

users = c.fetchall()
print(users)

db.execute("INSERT INTO USERS VALUES(?,?)",
		(password, password))