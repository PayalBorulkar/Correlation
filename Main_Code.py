import numpy as np
import pandas as pd
import sqlite3

#Taking CSV files as input
frame=pd.read_csv('user_course_views.csv')
interest=pd.read_csv('user_interests.csv')
assessment=pd.read_csv('user_assessment_scores.csv')
data=pd.read_csv('course_tags.csv')


#Displaying number of Unique users
frame_user=frame['user_handle'].nunique()

#Performing Data Processing (converting string to numbers and removing)
def Tran_maths(x):
    if(x=='Beginner'):
        return 2
    if(x=='Intermediate'):
        return 1
    if(x=='Advanced'):
        return 0
frame['level_values']=frame['level'].apply(Tran_maths)
def sentence(x):
    y=''.join(e for e in x if e.isalnum())
    return y

frame['view_date']=frame['view_date'].apply(sentence)
frame['course_id']=frame['course_id'].apply(sentence)
interest['interest_tag']=interest['interest_tag'].apply(sentence)
frame['view_date'] = frame['view_date'].astype('str').astype('int')

#Building Utility Matrix
frame_crosstab=pd.pivot_table(data=frame,values='view_time_seconds',index='course_id',columns='user_handle')

#Finding Correlation between Users based upon course viewed and storing the correlation values in Database
connex = sqlite3.connect("My_Database.db")  
cur = connex.cursor()  

for column in frame_crosstab:
    user=frame_crosstab[column]
    user[user>=10]
    similar_to_user=frame_crosstab.corrwith(user)
    corr_user=pd.DataFrame(similar_to_user,columns=['PearsonR']) #Pearson Correlation
    corr_user.dropna(inplace=True)
    corr_user.insert(loc=1,column='User',value=column)
    corr_user.to_sql('corr_user',con=connex,if_exists="append")
    connex.commit()
    
cur.close()
connex.close()
    














