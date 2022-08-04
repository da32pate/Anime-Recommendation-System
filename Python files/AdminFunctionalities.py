import sys
import os
import textwrap
import mysql.connector
from SQLConnection import *
from prettytable import PrettyTable
from datetime import datetime

#Code for Admin to insert values into sql tables
def InsertRecords():
    os.system('cls')
    print("Press 1 to insert into the table AnimeInfo")
    print("Press 2 to insert into the table UserInfo")
    print("Press 0 to exit")
    UserChoice=int(input("Please enter your choice: "))
    if(UserChoice==0):
        return 0

    elif(UserChoice==1):
        MALID = input("Input MALID: ")
        while (1):
            if (MALID.isdigit()):
                break
            else:
                MALID = input("Wrong input! Please enter a valid MALID: ")
        Name=input("Input Anime Name: ")
        while(1):
            Score = input("Input Anime score: ")
            try:
                Score = float(Score)
                if (isinstance(Score,int) or isinstance(Score,float)):
                    break
            except ValueError:
                print("Wrong input!")
        EnglishName = input("Input Anime English Name: ")
        Type = input("Input Anime Type: ")
        Episodes = input("Input Anime Episodes: ")
        while (1):
            if (Episodes.isdigit()):
                break
            else:
                Episodes = input("Wrong input! Please enter a valid Episodes value: ")
        format = "%Y-%m-%d"
        AiredStr=input("Input Anime Aired_start: ")
        while(1):
            try:
                if(bool(datetime.strptime(AiredStr,format))==True):
                    AiredStart=AiredStr
                    break
            except ValueError:
                AiredStr = input("Wrong input! Please enter a valid Date in the YYYY-MM-DD format: ")
        AiredEndStr = input("Input Anime Aired_end: ")
        while (1):
            try:
                if (bool(datetime.strptime(AiredEndStr,format))==True):
                    AiredEnd = AiredEndStr
                    break
            except ValueError:
                AiredEndStr = input("Wrong input! Please enter a valid Date in the YYYY-MM-DD format: ")
        Duration_in_min_per_episode = input("Input Duration_in_min_per_episode: ")
        while (1):
            if (Duration_in_min_per_episode.isdigit()):
                break
            else:
                Duration_in_min_per_episode = input("Wrong input! Please enter a valid Duration value: ")
        Popularity = int(input("Input Popularity: "))
        while (1):
            if (isinstance(Popularity,int)):
                break
            else:
                Popularity = input("Wrong input! Please enter a valid Popularity value: ")
        args=MALID, Name, Score, EnglishName, Type, Episodes, AiredStart, AiredEnd, Duration_in_min_per_episode, Popularity
        try:
            AnimeInfoInsertQuery = "Insert into AnimeInfo(MALID, Name, Score, EnglishName,Type, Episodes, \
                                    Aired_start,Aired_end, Duration_in_min_per_episode, Popularity) \
                                    Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor= mydb.cursor()
            mycursor.execute(AnimeInfoInsertQuery, args)
            mydb.commit()
            print(mycursor.rowcount, " row inserted successfully")
            ch=int(input("Press 0 to exit: "))
            if(ch==0):
                return 0
            mycursor.close()

        except mysql.connector.IntegrityError as ie:
            print("Failed to insert values...!!", ie)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        except mysql.connector.errors.DatabaseError as er:
            print("Error: {}".format(er))
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

    elif(UserChoice==2):
        flag=0
        os.system('cls')
        while(1):
            role =input("Enter user role to be inserted: ")
            if(role!='Register User' and role!='Admin User'):
                UserChoice=int(input("Invalid role entered. Please try again or press 0 to exit: "))
                if UserChoice==0:
                    flag = 1
                    break
            else:
                break

        if (flag==0):
            lastrow="SELECT * FROM userinfo WHERE userid=(SELECT max(userid) FROM userinfo);"
            mycursor = mydb.cursor()
            mycursor.execute(lastrow)
            lastentry=mycursor.fetchall()
            for l in lastentry:
                lastUid=int(l[0])

            UserInfoInsertQuery="Insert into UserInfo values ("+str(lastUid+1)+", "+str(lastUid+1)+", \'"+role+"\');"
            try:
                mycursor.execute(UserInfoInsertQuery)
                mydb.commit()
                print(mycursor.rowcount," row inserted successfully")
                print("User ID: ",lastUid," Password: ",lastUid)
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0
                mycursor.close()
            except mysql.connector.IntegrityError as ie:
                print("Failed to insert values...!!", ie)
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0

            except mysql.connector.errors.DatabaseError as er:
                print("Error: {}".format(er))
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0

#Code for Admin to update records in sql table
def UpdateRecords():
    os.system('cls')
    while(1):
        MALID=int(input("Enter MALID to update record in AnimeInfo table: "))
        if (isinstance(MALID, int)):
            break
        else:
            MALID = input("Wrong input! Please enter a valid MALID: ")

    AttributeName=input("Enter the Name of the attribute to be updated: ")
    AttributeValue=input("Enter the value of the attribute to be updated: ")

    SearchQuery="Select * from animeinfo where MALID="+str(MALID)+";"
    try:
        mycursor=mydb.cursor(buffered=True)
        mycursor.execute(SearchQuery)
        if(mycursor.rowcount==0):
            print("No records found with the provided MALID")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0
            mycursor.close()
        else:
            UpdateQuery="Update AnimeInfo set "+str(AttributeName)+"=\'"+str(AttributeValue)+"\' where MALID="+str(MALID)+";"
            try:
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute(UpdateQuery)
                mydb.commit()
                print("Successfully updated ",mycursor.rowcount,"records")
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0
                mycursor.close()
            except mysql.connector.IntegrityError as ie:
                print("Failed to insert values...!!",ie)
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0

            except mysql.connector.errors.DatabaseError as er:
                print("Error: {}".format(er))
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0

    except mysql.connector.IntegrityError as ie:
        print("Failed to insert values...!!",ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

    except mysql.connector.errors.DatabaseError as er:
        print("Error: {}".format(er))
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

#Code for Admin to delete a record from sql table
def DeleteRecord():
    os.system('cls')
    uid = int(input("Enter UserID to delete a record from the UserInfo table: "))
    UserDeleteQuery = "Delete from UserInfo where UserID=" + str(uid) + ";"
    try:
        mycursor = mydb.cursor()
        mycursor.execute(UserDeleteQuery)
        mydb.commit()
        print("Record deleted successfully..")
        mycursor.close()
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

    except mysql.connector.IntegrityError as ie:
        print("Failed to insert values...!!",ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

    except mysql.connector.errors.DatabaseError as er:
        print("Error: {}".format(er))
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

#Admin user options
def AdminLogin():
    while(1):
        os.system('cls')
        print("Welcome Admin")
        print("Press 1 to insert record")
        print("Press 2 to update record")
        print("Press 3 to delete record")
        print("Print 0 to exit")
        UserChoice = int(input("Please select one option: "))

        if(UserChoice==0):
           break

        elif(UserChoice==1):
            InsertRecords()

        elif(UserChoice==2):
            UpdateRecords()

        elif(UserChoice==3):
            print("Delete Record")
            DeleteRecord()
