# ---------------------------------------------
# This program for password and user => python
# ---------------------------------------------


# first import getpass
import getpass

database = {"ahmed": "123", "yossef": "456", "farouk": "789"}


user_input = input("Enter your username: ")

# getpass for hide password
password = getpass.getpass("Enter your password: ")

# for loop for check username and password
for i in database.keys():

    # if user_input == i and password == database[i]: in database.keys():
    if user_input == i:
        while password != database[i]:
            print("Wrong password")
            password = getpass.getpass("Enter your password: ")
    else:
        print("Wrong username")
        break
else:
    print("Welcome to your account")
    print("verified")
