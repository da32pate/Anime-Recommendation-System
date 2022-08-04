import csv
import pandas as pd
#see = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\rating_complete.csv")
with open(r"C:\Fall21\ECE656\project_dataset\rating_complete.csv",'r') as file:
	data = file.readlines()
df=pd.DataFrame(data)
# print(df)
lastRow = data[-1]
lastRow=lastRow.split(",")
lastUser = int(lastRow[0])
# print(type(lastUser))

with open('UserInfo.csv', 'w',newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                             quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['UserID', 'Password', 'Role'])
    for i in range(0,lastUser+1):
        filewriter.writerow([i,i,'Registered User'])