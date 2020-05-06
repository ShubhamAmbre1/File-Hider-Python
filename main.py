import sqlite3
import hashlib


def dec(func):
	def wrapper():
		check_password = hashlib.sha256(input("Enter password : ").encode('ascii')).hexdigest()
		if check_password == create_password:
			return func()
		else:
			print("Invalid Password")
			return wrapper()
	return wrapper

def create_hider():
	
	path = input("""
	****************************************
	Enter path where you want to hide files
	example : C:/Users/Pc/Desktop/
	"Put '/' at the end"
	: 
		""")
	global create_password
	create_password = hashlib.sha256(input("Enter a password : ").encode('ascii')).hexdigest()

	conn = sqlite3.connect('fh.db')

	c = conn.cursor()

	c.execute("""CREATE TABLE files(
		password text,
		file BLOB NOT NULL
		)""")

	conn.commit()

	conn.close()

def add_file():
	pass

def remove_file():
	pass

def delete_hider():
	pass





if __name__ == "__main__":
	i = int(input("""
************************************

1 = Create Hider
2 = Open Hider
2 = Add File
3 = Remove File
4 = Delete Hider
5 = Exit

************************************
= """))
	while True:
		if i == 1:
			try:
				create_hider()
			except:
				print("Already created")
				continue

		elif i == 2:
			try:
				add_file()
			except:
				print("Already exist")

		elif i == 3:
			try:
				remove_file()
			except:
				print("No such file")

		elif i == 4:
			try:
				delete_hider()
			except:
				print("No such Hider")
		elif i == 5:
			quit()

