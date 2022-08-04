import numpy as np
import pandas as pd
data1 = pd.read_csv('C:\Fall21\ECE656\project_dataset\\anime.csv')
data2 = pd.read_csv('C:\Fall21\ECE656\project_dataset\\anime_with_synopsis.csv')
data2=data2.drop(['Name', 'Score', 'Genres'], axis=1)

print(data2)
#output1 = data1.merge(data2,
 #                  left_on='MAL_ID',right_index=True)
# output1=data1.merge(data2, how='left', on='MAL_ID')
output=data1.set_index('MAL_ID').join(data2.set_index('MAL_ID'))
output.loc[pd.isnull(output['sypnopsis']) == True, 'sypnopsis'] = 'NULL'
# print(output1)
print(output)
output.to_csv('anime1.csv',index=True)