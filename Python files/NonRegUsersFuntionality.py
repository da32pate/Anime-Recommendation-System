import sys
import os
import mysql.connector
from SQLConnection import *
from prettytable import PrettyTable

# Code to search Animes based on Anime Name
def SearchByAnimeNameNonRegUser():
    os.system('cls')
    AnimeName = input("Please type anime name to search: ")
    #Query string to fetch results
    UserAnimeQuery = "Select Name,Score,Episodes,Aired_start from Anime_View_NonRegUser where Name like \'" + AnimeName + "%\';"
    try:
        mycursor=mydb.cursor()
        mycursor.execute(UserAnimeQuery)
        animes = mycursor.fetchall()
        ColumnName=["Name", "Score","Episodes","Released Date"]
        display = PrettyTable()
        #If no record found
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        #If more than 10 results found
        elif (mycursor.rowcount > 10):
            nextCount = 0
            r = int((mycursor.rowcount / 10) if (mycursor.rowcount % 10 == 0) else int((mycursor.rowcount / 10)) + 1)
            for i in range(0, r, 1):
                display.field_names = ColumnName
                k = nextCount * 10
                l = k + 10
                for j in range(k, min(l, len(animes)), 1):
                    display.add_row(animes[j])

                nextCount = nextCount + 1
                os.system('cls')
                print(display)
                display.clear()
                if (r > 0):
                    print("Press 1 for next page")
                    print("Press 2 to exit")
                    tableViewInput = int(input("Chose one option: "))
                    if (tableViewInput == 1):
                        os.system('cls')
                        continue
                    elif (tableViewInput == 2):
                        os.system('cls')
                        break
                    else:
                        print("Wrong choice..")

        # If less than 10 results found
        else:
            display.field_names = ColumnName
            for r in animes:
                display.add_row(r)

            print(display)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        mycursor.close()
    #Catch sql exceptions/errors
    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!", ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

# Code to search Animes based on Anime Age rating
def SearchByAnimeRatingNonRegUser():
    os.system('cls')
    #Fetch Age ratings available in the DB
    UserAnimeQuery = "Select DISTINCT Rating from Anime_View_NonRegUser where Rating is not NULL;"
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(UserAnimeQuery)
    animes = mycursor.fetchall()
    items = tuple(list(list(zip(*animes))[0]))
    for a in range(0,len(items),1):
        print("Press ", a+1," to search animes with rating ",items[a])
    UserChoice=int(input("Please select one option: "))
    ch=items[UserChoice-1]
    #Code to fetch Animes based on Age rating selected by the user
    AnimeByRatingQuery="Select Name,Rating from Anime_View_NonRegUser where Rating=\'"\
                       +str(ch)+"\';"
    print(AnimeByRatingQuery)
    try:
        mycursor.execute(AnimeByRatingQuery)
        results=mycursor.fetchall()
        ColumnName=["Anime Name","Rating"]
        display = PrettyTable()
        #If no record found
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        #If more than 10 results found
        elif (mycursor.rowcount > 10):
            nextCount = 0
            r = int((mycursor.rowcount / 10) if (mycursor.rowcount % 10 == 0) else int((mycursor.rowcount / 10)) + 1)
            for i in range(0, r, 1):
                display.field_names = ColumnName
                k = nextCount * 10
                l = k + 10
                for j in range(k, min(l, len(results)), 1):
                    display.add_row(results[j])

                nextCount = nextCount + 1
                os.system('cls')
                print(display)
                display.clear()
                if (r > 0):
                    print("Press 1 for next page")
                    print("Press 2 to exit")
                    tableViewInput = int(input("Chose one option: "))
                    if (tableViewInput == 1):
                        os.system('cls')
                        continue
                    elif (tableViewInput == 2):
                        os.system('cls')
                        break
                    else:
                        print("Wrong choice..")

        # If less than 10 results found
        else:
            display.field_names = ColumnName
            for r in results:
                display.add_row(r)

            print(display)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        mycursor.close()
    #Catch SQL exceptions
    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!", ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

#Code to search Animes based on relase Date
def SearchByAnimeReleaseDateNonRegUser():
    os.system('cls')
    AiredStart = input("Please type the 1st relase date of anime in (YYYY-MM-DD) format: ")
    while(1):
        if(AiredStart!=""):
            break
        else:
            os.system('cls')
            AiredStart = input("Please enter at least the 1st relase date of anime in (YYYY-MM-DD) format: ")

    AiredEnd =input("Please type the 2nd relase date of anime in (YYYY-MM-DD) format: ")
    if(AiredEnd!=""):
        SearchByDateQuery='Select Name,Aired_start from Anime_View_NonRegUser where Aired_start BETWEEN \''+AiredStart+'\' and \''+AiredEnd+'\';'

    else:
        SearchByDateQuery = 'Select Name,Aired_start from Anime_View_NonRegUser where Aired_start>=\'' + AiredStart + '\';'

    try:
        mycursor = mydb.cursor()
        mycursor.execute(SearchByDateQuery)
        animes = mycursor.fetchall()
        ColumnName=["Name", "Aired"]
        display = PrettyTable()
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        elif (mycursor.rowcount > 10):
            nextCount = 0
            r = int((mycursor.rowcount / 10) if (mycursor.rowcount % 10 == 0) else int((mycursor.rowcount / 10)) + 1)
            for i in range(0, r, 1):
                display.field_names = ColumnName
                k = nextCount * 10
                l = k + 10
                for j in range(k, min(l, len(animes)), 1):
                    display.add_row(animes[j])

                nextCount = nextCount + 1
                os.system('cls')
                print(display)
                display.clear()
                if (r > 0):
                    print("Press 1 for next page")
                    print("Press 2 to exit")
                    tableViewInput = int(input("Chose one option: "))
                    if (tableViewInput == 1):
                        os.system('cls')
                        continue
                    elif (tableViewInput == 2):
                        os.system('cls')
                        break
                    else:
                        print("Wrong choice..")

        else:
            display.field_names = ColumnName
            for r in animes:
                display.add_row(r)

            print(display)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        mycursor.close()

    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!",ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

#Non-registered user's search options
def AnimeSearch():
    while(1):
        os.system('cls')
        print("Press 1 to search anime by Name")
        print("Press 2 to search anime by Anime Age Rating")
        print("Press 3 to search anime by Release Date")
        print("Press 0 to exit")
        UserChoice = int(input("Please select one option: "))
        if(UserChoice==0):
            break

        elif (UserChoice == 1):
            SearchByAnimeNameNonRegUser()

        elif (UserChoice == 2):
            SearchByAnimeRatingNonRegUser()

        elif (UserChoice == 3):
            SearchByAnimeReleaseDateNonRegUser()

        else:
            print("Oops! Wrong input..")
