from cryptography.fernet import Fernet

master_pwd = input("What is the master password: ")

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User name:", user,"| Password:", passw)
    
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name +"|"+ pwd + "\n")
        

while True:
    mode = input("Would you like to add a password or View an existing on (View, Add)? Press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please select a correct option")
        continue
    