import pandas as pd
data = pd.read_csv('C:\Fall21\ECE656\project_dataset\\animelist.csv')


# data = pd.read_excel('C:\Temp\data.xlsx')
#print(data)
output=data.drop_duplicates()
output.to_csv('animelist1.csv',index=False)