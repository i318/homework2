from cgitb import text
from cryptography.fernet import Fernet




'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''



def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


master_pwd = input("What is the master password?:  ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw, phoneno = data.split("|")
            print("User:", user, "| Password: ", fer.decrypt(passw.encode()), "| Phone Number: ", phoneno)




def add():
    name = input("Account name: ")
    pwd = input("Password: ") 
    phonenumber = input("Phome number: ")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + phonenumber + "\n")






while True:
    mode = input("Would you like to add a new password and phone number or view existing ones? (view/add), press q to quit: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode =="add":
        add()
    else:
        print("Invalid.")