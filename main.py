import sqlite3
import hashlib


def dec(func):
    def pass_checker():
        conn = sqlite3.connect('fh.db')
        c = conn.cursor()
        c.execute("SELECT password FROM passw")
        conn.commit()
        check = c.fetchone()

        check_password = hashlib.sha256(input("Enter password : ").encode('ascii')).hexdigest()
        # check_password = input()
        print(check[0],'\n', check_password)
        if check_password == check[0]:
            return func()
        else:
            print("Invalid Password")
            return pass_checker()
    return pass_checker



def create_hider():

    conn = sqlite3.connect('fh.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE files(
        file BLOB NOT NULL
        )""")
    conn.commit()

    print("Hider Created")

    create_password = hashlib.sha256(input("Enter a password : ").encode('ascii')).hexdigest()
    # create_password = input()
    c.execute("CREATE TABLE passw(password TEXT)")   
    conn.commit() 

    c.execute("INSERT INTO passw(password) VALUES(:passwo)",{'passwo': create_password})
    conn.commit()

    conn.close()



@dec
def add_file():
    print('Complete')

@dec
def remove_file():
    pass

@dec
def delete_hider():
    pass


if __name__ == "__main__":
#     path = input("""
# ****************************************
# Enter hider destination
# example : C:/Users/Pc/Desktop/
# "Put '/' at the end"
# : """)

    while True:
        i = int(input("""
************************************

1 = Create Hider
2 = Add File
3 = Remove File
4 = Delete Hider
5 = Exit

************************************
= """))
    
        if i == 1:
            try:
                create_hider()
            except:
                print("Already created!")
        
        elif i == 2:
            add_file()
            
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

