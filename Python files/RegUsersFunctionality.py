import sys
import os
import textwrap
import mysql.connector
from SQLConnection import *
from prettytable import PrettyTable

# Code to search Animes based on Anime Name
def SearchByAnimeName():
    os.system('cls')
    AnimeName = input("Please type anime name to search: ")
    # Query string to fetch results
    UserAnimeQuery = 'Select Name,Score,Episodes,Aired_start,Rating from AnimeInfo where Name like \'' + AnimeName + '%\';'
    try:
        mycursor = mydb.cursor()
        mycursor.execute(UserAnimeQuery)
        animes = mycursor.fetchall()
        ColumnName=["Name", "Score","Episodes","Released Date","Rating"]
        display = PrettyTable()
        # If no record found
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        # If more than 10 results found
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

    # Catch sql exceptions/errors
    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!",ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

#Code to search Animes based on score
def SearchByAnimeUserRating():
    os.system('cls')
    print("Press 1 see the animes with Score between 9-10")
    print("Press 2 see the animes with Score between 8-9")
    print("Press 3 see the animes with Score between 7-8")
    print("Press 4 see the animes with Score between 6-7")
    print("Press 5 see the animes with Score between 5-6")
    print("Press 0 to exit")
    UserChoice = int(input("Please enter your choice: "))
    if(UserChoice==1):
        SearchByAnimeRatingQuery="Select Name,Score from AnimeInfo where Score>=9 and Score<=10;"

    elif (UserChoice == 2):
        SearchByAnimeRatingQuery = "Select Name,Score from AnimeInfo where Score>=8 and Score<=9;"

    elif (UserChoice == 3):
        SearchByAnimeRatingQuery = "Select Name,Score from AnimeInfo where Score>=7 and Score<=8;"

    elif (UserChoice == 4):
        SearchByAnimeRatingQuery = "Select Name,Score from AnimeInfo where Score>=6 and Score<=7;"

    elif (UserChoice == 5):
        SearchByAnimeRatingQuery = "Select Name,Score from AnimeInfo where Score>=5 and Score<=6;"

    try:
        mycursor = mydb.cursor()
        mycursor.execute(SearchByAnimeRatingQuery)
        animes = mycursor.fetchall()
        display = PrettyTable()
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        elif (mycursor.rowcount > 10):
            nextCount = 0
            r=int((mycursor.rowcount / 10) if (mycursor.rowcount % 10==0) else int((mycursor.rowcount / 10))+1)
            for i in range(0, r, 1):
                display.field_names = ["Name", "Score"]
                k = nextCount * 10
                l=k+10
                for j in range(k, min(l,len(animes)), 1):
                    display.add_row(animes[j])

                nextCount = nextCount + 1
                os.system('cls')
                print(display)
                display.clear()
                if (r>0):
                    print("Press 1 for next page")
                    print("Press 2 to exit")
                    tableViewInput = int(input("Chose one option: "))
                    if (tableViewInput == 1):
                        os.system('cls')
                        continue
                    elif(tableViewInput==2):
                        os.system('cls')
                        break
                    else:
                        print("Wrong choice..")

        else:
            print(mycursor.rowcount, " number of records found")
            display.field_names = ["Name", "Score"]
            for anime in animes:
                display.add_row(anime)

            print(display)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0
        mycursor.close()

    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!",ie)

#Code to search Animes based on Genres
def SearchByAnimeByGenre():
    #Code to fetch different Genres available in the DB
    GenreList="Select distinct Genre from Genre;"
    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute(GenreList)
        genres = mycursor.fetchall()
        display = PrettyTable()
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0
        else:
            print("List of available Genres")
            display.field_names =["Genres"]
            for genre in genres:
                display.add_row(genre)

            print(display)
            mycursor.close()
    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!",ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

    #Code to prepare a Genre Name list seperated by ,
    GenreInput=input("Enter the genres seperated by , to search anime:")
    G_list=GenreInput.split(",")
    tempG=""
    if(len(G_list)>1):
        for g in range(0,len(G_list),1):
            if(g==len(G_list)-1):
                tempG=tempG+G_list[g]+"\'"
            else:
                tempG = tempG + G_list[g] + "\' OR Genre=\'"
    else:
        tempG=str(G_list[0])

    #Code to fecth animes based on user Genre input
    if(len(G_list)==1):
        GenreQuery="SELECT Distinct Name from AnimeInfo INNER join Genre on AnimeInfo.MALID=Genre.MALID"\
                   " where Genre =\'"+str(tempG)+"\';"

    else:
        GenreQuery = "SELECT Distinct Name from AnimeInfo INNER join Genre on AnimeInfo.MALID=Genre.MALID"\
                     " where Genre =\'" + str(tempG) + ";"

    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute(GenreQuery)
        animes = mycursor.fetchall()
        ColumnName=["Anime Name"]
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
            print(mycursor.rowcount, " number of records found")
            display.field_names = ColumnName
            for anime in animes:
                display.add_row(anime)

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

#Code to seach Anime based on popularity
def SearchForTrendingAnime():
    os.system('cls')
    limit=input("Please enter how many trending Anime you want to view: ")
    TrendingAnimeQuery="Select DISTINCT Name from AnimeInfo order by popularity DESC limit "+str(limit)+";"
    try:
        mycursor = mydb.cursor()
        mycursor.execute(TrendingAnimeQuery)
        animes = mycursor.fetchall()
        ColumnName=["Name"]
        display = PrettyTable()

        if (mycursor.rowcount == 0):
            print("Oops! No record found...")

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
            for anime in animes:
                display.add_row(anime)

            print(display)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        mycursor.close()

    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!", ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0

#Code to fetch synopsis of an Anime
def FetchSynopsis():
    os.system('cls')
    AnimeName = input("Please type anime name to search: ")
    UserAnimeQuery = 'Select Name,Synopsis from AnimeInfo where Name like \'' + AnimeName + '%\';'

    try:
        mycursor = mydb.cursor()
        mycursor.execute(UserAnimeQuery)
        animes = mycursor.fetchall()
        if (mycursor.rowcount == 0):
            print("Oops! No record found...")
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0


        elif (mycursor.rowcount > 10):
            nextCount = 0
            r = int((mycursor.rowcount / 10) if (mycursor.rowcount % 10 == 0) else int((mycursor.rowcount / 10)) + 1)
            for i in range(0, r, 1):
                print("Anime Name")
                print("------------------")
                k = nextCount * 10
                l = k + 10
                for j in range(k, min(l, len(animes)), 1):
                    print(animes[j][0])

                print("------------------")
                nextCount = nextCount + 1
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
            os.system('cls')

            print("Anime Name")
            print("------------------")
            for (Name,Synopsis) in animes:
                print(Name)
            print("------------------")

        A_Name = input("Enter anime name to read synopsis: ")
        for (Name, Synopsis) in animes:
            if (A_Name == Name):
                print("Synopsis: ", end="")
                print(textwrap.fill(Synopsis, 100))
                ch=int(input("Press 0 to exit"))

                if(ch==0):
                    return 0

        mycursor.close()
    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!", ie)
        ch = int(input("Press 0 to exit"))

        if (ch == 0):
            return 0

#Code to modify the rating of an Anime that the user had watched and rated previously
def RateAnime(UserID):
    os.system('cls')
    print("List of Animes that you have watched and rated..")
    AnimeRatingQuery="Select AnimeInfo.Name, AnimeRatingComplete.Rating,AnimeRatingComplete.MALID from AnimeInfo INNER JOIN AnimeRatingComplete"\
                         " on AnimeInfo.MALID=AnimeRatingComplete.MALID where UserID="+str(UserID)+";"

    try:
        mycursor = mydb.cursor()
        mycursor.execute(AnimeRatingQuery)
        animes = mycursor.fetchall()
        display = PrettyTable()

        if (mycursor.rowcount == 0):
            print("Oops! No record found...")

        elif (mycursor.rowcount > 10):
            nextCount = 0
            r = int((mycursor.rowcount / 10) if (mycursor.rowcount % 10 == 0) else int((mycursor.rowcount / 10)) + 1)
            for i in range(0, r, 1):
                display.field_names = ["Name", "Rating"]
                k = nextCount * 10
                l = k + 10
                for j in range(k, min(l, len(animes)), 1):
                    t=animes[j]
                    display.add_row([t[0],t[1]])

                nextCount = nextCount + 1
                #os.system('cls')
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
            print(mycursor.rowcount, " number of records found")
            display.field_names = ["Name", "Rating"]
            for anime in animes:
                display.add_row(anime)

            print(display)
            ch = int(input("Press 0 to exit: "))
            if (ch == 0):
                return 0

        mycursor.close()

    except mysql.connector.IntegrityError as ie:
        print("Failed to fetch values...!!", ie)
        ch = int(input("Press 0 to exit: "))
        if (ch == 0):
            return 0
    AnimeName = input("Enter the anime name to modify the rating: ")
    UserRating = int(input("Enter a score between 0-10: "))
    for(Name,Rating,MALID) in animes:
        if(AnimeName==Name):
            UpdateRatingQuery="Update AnimeRatingComplete set Rating="+str(UserRating)+" where"\
                                " MALID="+str(MALID)+" and UserID="+str(UserID)+";"

            try:
                mycursor=mydb.cursor()
                mycursor.execute(UpdateRatingQuery)
                animeUpdate = mycursor.fetchall()
                mydb.commit()
                print("Rating for ",AnimeName," updated successfully!!")
                mycursor.close()
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0

            except mysql.connector.IntegrityError as ie:
                print("Failed to update record...!!",ie)
                ch = int(input("Press 0 to exit: "))
                if (ch == 0):
                    return 0

#Code for registered user search/modify options
def RegUserLogin(UserID):
    while (1):
        os.system('cls')
        print("Welcome Registered User")
        print("Press 1 to search Anime")
        print("Press 2 to search Animes based on Anime Score")
        print("Press 3 to search Animes based on Genres")
        print("Press 4 to search for Trending Anime")
        print("Press 5 to read synopsis of Anime")
        print("Press 6 to modify your Anime Rating")
        print("Press 0 to exit")
        UserChoice = int(input("Please select one option: "))
        if (UserChoice == 0):
            break

        elif (UserChoice == 1):
            SearchByAnimeName()

        elif(UserChoice==2):
            SearchByAnimeUserRating()

        elif(UserChoice==3):
            SearchByAnimeByGenre()

        elif (UserChoice == 4):
            SearchForTrendingAnime()

        elif (UserChoice == 5):
            FetchSynopsis()

        elif(UserChoice==6):
            RateAnime(UserID)