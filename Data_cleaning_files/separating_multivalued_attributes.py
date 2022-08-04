import pandas as pd
import numpy as np
see = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\anime.csv")
df=pd.DataFrame(see)
# Exploding into multiple cells, We start with creating a new dataframe from the series with Id as the index
new_df = pd.DataFrame(df.Genres.str.split(',').tolist(), index=df.MAL_ID).stack()
# We now want to get rid of the secondary index
# To do this, we will make Id as a column (it can't be an index since the values will be duplicate)
new_df = new_df.reset_index([0, 'MAL_ID'])
# The final step is to set the column names as we want them
new_df.columns = ['MAL_ID', 'Genres']
# print(new_df)
new_df.to_csv('Genre.csv',index=False)
see_1 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\Genre.csv")
df_1=pd.DataFrame(see_1)
df_1['Genres'] = df_1['Genres'].str.lstrip()

df_1.to_csv('Genre.csv',index=False)


#PRODUCERS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
see2 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\anime.csv")
df2=pd.DataFrame(see2)
new_df2 = pd.DataFrame(df2.Producers.str.split(',').tolist(), index=df2.MAL_ID).stack()

print(new_df2)
new_df2 = new_df2.reset_index([0, 'MAL_ID'])
new_df2.columns = ['MAL_ID', 'Producers']
new_df2.to_csv('Producers.csv',index=False)
see2_1 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\Producers.csv")
df2_1=pd.DataFrame(see2_1)
df2_1['Producers'] = df2_1['Producers'].str.lstrip()
df2_1.to_csv('Producers.csv',index=False)


#LICENSORS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
see3 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\anime.csv")
df3=pd.DataFrame(see3)
new_df3 = pd.DataFrame(df3.Licensors.str.split(',').tolist(), index=df3.MAL_ID).stack()
new_df3 = new_df3.reset_index([0, 'MAL_ID'])
new_df3.columns = ['MAL_ID', 'Licensors']
new_df3.to_csv('Licensors.csv',index=False)
#removing leading whitespaces
see3_1 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\Licensors.csv")
df3_1=pd.DataFrame(see3_1)
df3_1['Licensors'] = df3_1['Licensors'].str.lstrip()
df3_1.to_csv('Licensors.csv',index=False)


# #STUDIOS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
see4 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\anime.csv")
df4=pd.DataFrame(see4)
new_df4 = pd.DataFrame(df4.Studios.str.split(',').tolist(), index=df4.MAL_ID).stack()
new_df4 = new_df4.reset_index([0, 'MAL_ID'])
new_df4.columns = ['MAL_ID', 'Studios']
new_df4.to_csv('Studios.csv',index=False)
#removing leading white spaces
see4_1 = pd.read_csv(r"C:\Fall21\ECE656\project_dataset\Studios.csv")
df4_1=pd.DataFrame(see4_1)
df4_1['Studios'] = df4_1['Studios'].str.lstrip()
df4_1.to_csv('Studios.csv',index=False)
