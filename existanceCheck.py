import sqlite3

db = sqlite3.connect('practice.db')
c = db.execute("SELECT * FROM users")

password = "lmao123"
randomUsernames = ['mahand1','mahand2','elamino','elamine',
				'paserie','elias','rub','yeetah','admo',
				'ilyas','elaminio','mouad','ben','ethan',
				'mina','adam','elliot','tiany','adnan']
existingUser = 'elamine'




#db.execute('''CREATE TABLE USERS
		#(USERNAME TEXT NOT NULL,
		#PASSWORD TEXT NOT NULL);''')






#for user in randomUsernames:
	#db.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES(?,?)",
		#(user, password))
db.commit()	

users = c.fetchall()

check = False
#check if user exists
for user in users:
	for elem in user:
		print(elem)
		if elem == existingUser:
			check = True

print("This should be True: " + str(check))

