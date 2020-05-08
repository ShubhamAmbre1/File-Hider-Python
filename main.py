import sqlite3
import hashlib
import os

def dec(func):
    def pass_checker():
        global conn,c
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("SELECT password FROM passw")
        conn.commit()
        check = c.fetchone()
        check_password = hashlib.sha256(input("Enter password : ").encode('ascii')).hexdigest()
        if check_password == check[0]:
            return func()
        else:
            print("Invalid Password")
            return pass_checker()
    return pass_checker


def create_hider():

    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("""CREATE TABLE files(
        name TEXT,
        file BLOB NOT NULL
        )""")
    conn.commit()

    print("Hider Created")

    create_password = hashlib.sha256(input("Enter a password : ").encode('ascii')).hexdigest()

    c.execute("CREATE TABLE passw(password TEXT)")   
    conn.commit() 

    c.execute("INSERT INTO passw(password) VALUES(:passwo)",{'passwo': create_password})
    conn.commit()

    conn.close()


@dec
def add_file():
    file = input("Enter file path = ")
    lis = file.split("/") 
    
    with open(file, 'rb') as f:
        data = f.read()

    c.execute("INSERT INTO files(name, file) VALUES(:name ,:file)",{'name':lis[len(lis)-1:][0], 'file': data})
    print("File added.")

    conn.commit()
    conn.close()
    

@dec
def remove_file():
    name = input("Enter the file name = ")

    c.execute("SELECT name,file FROM files WHERE name = (:name)",{'name': name})

    content = c.fetchone()
    with open(name, 'wb') as f:
        f.write(content[1])
    conn.commit()

    c.execute("DELETE FROM files WHERE name = (:name)", {'name': name})
    conn.commit()
    c.execute("VACUUM")
    print(f"Removed {name}")
    conn.commit()
    conn.close()


@dec
def delete_hider():
    conn.close()
    path_list = path.split("/")
    name = path_list[len(path_list)-1:][0]
    print("{} will be deleted".format(name[:len(name)-3]))
    x = input("""Are you sure?
Y/N = """)

    if x == 'y' or x == 'Y':
        os.remove(path)


if __name__ == "__main__":
    path = input("""
****************************************
Enter hider destination and name
example : C:/Users/Pc/Desktop/hider.db
: """)
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

