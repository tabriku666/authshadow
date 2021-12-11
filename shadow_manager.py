import scrypt

store_user = ("")
store_password = ("")

class userlogin():
	global store_user
	global store_password
	def user_password_create():
		print ("Create account first!")
		global store_user
		global store_password
		user = input ("Username: ")
		password = input ("Password: ")
		store_user += user
		store_password += password
	
	def user_password_login():
		print ("Please login!")
		global store_user
		global store_password

		
		
class simpledb():
	def user_store():
		global store_user
		global store_password
		with open(store_user, 'w') as file:
			file.write(store_password)


userlogin.user_password_create()
simpledb.user_store()