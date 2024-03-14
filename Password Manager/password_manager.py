from cryptography.fernet import Fernet

# Now using the cryptography module we are going to encrypt our txt file

"""
def  write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: #'wb' = write bite 
            key_file.write(key)

write_key()  #- by calling the function we can check how the key file gets created
"""

def load_key():
    
    file = open('key.key', 'rb') # 'rb' = read mode in binary
    key = file.read()
    file.close()
    return key

""" we need a master password that will allow user to 
access the password file"""

master_pwd = input("Please enter a master password: ")
# This password will show correct password if entered correct password, otherwise wrongs passwords will be displayed

key = load_key() + master_pwd.encode()
fer = Fernet(key)
#Here we are converting the master_password in bytes format and using it as key 

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user : ", user,"| Password : ", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f: # Here 'a'= append mode, 'w' = write mode, 'r' = read only mode  
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(" Would you like to add a new password or view exising, choosw(view, add) or press 'q' for exit: ").lower()
    
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue

# mast pass = pass