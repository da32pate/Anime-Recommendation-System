import getpass
import os
import sys
from SQLConnection import *
from NonRegUsersFuntionality import *
from RegUsersFunctionality import *
from AdminFunctionalities import *

# Code for User login
def UserLogin():
    os.system('cls')
    uid=input("Please enter User ID:")
    while(1):
        if(uid!=""):
            break
        else:
            os.system('cls')
            uid = input("User ID is required to Login! Please enter User ID:")

    pwd = getpass.getpass('Please enter password:')
    while(1):
        if(pwd!=""):
            break
        else:
            pwd = getpass.getpass('Password is required to Login! Please enter password:')

    UserInfoQuery='Select * from UserInfo where UserID='+uid+' and Password='+pwd+';'
    try:
        mycursor.execute(UserInfoQuery)
        users = mycursor.fetchall()
        if(mycursor.rowcount==1):
            for user in users:
                UserRole =user[2]

            UserRole=UserRole.replace('\r', '')
            if(UserRole=="Admin User"):
                 AdminLogin()

            elif(UserRole=="Registered User"):
                RegUserLogin(uid)
        else:
            print("Error: Unsuccessful")

    except mysql.connector.IntegrityError:
        print("Failed to fetch values...!!")

# Code for User Search options
def SearchOptions(opt):
    if(opt==1):
        UserLogin()

    elif(opt==2):
        AnimeSearch()

    else:
        os.system('cls')
        print("Oops! Wrong input..")

# Main Code
if __name__=="__main__":
    if(mydb.is_connected()):
        print("Connected to the server..")
        while (1):
            try:
                os.system('cls')
                print("Press 1 to login")
                print("Press 2 to search anime")
                print("Press 0 to exit")
                opt = int(input("Please select one option:"))
                if (opt == 0):
                    exit()
                else:
                    SearchOptions(opt)
            except ValueError:
                os.system('cls')
                print("Oops! Wrong input..")

    else:
        print("Not connected")
        
