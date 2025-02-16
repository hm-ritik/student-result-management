print("Hi we are Dving into Our first Project")
import numpy as np
import pandas as pd
import random

data={
    'Name':['Ravi' , 'Sia' , 'Ritik' , 'rohit' , 'Love' , 'Kush' , 'Ram', 'Lucky'],
    'Age': np.random.randint(18,22 , size=8),
    'Dsa': np.random.randint(8,31, size=8),
    'Maths': np.random.randint(8,31, size=8),
    'Oops': np.random.randint(8,31, size=8),
    'DE': np.random.randint(8,31, size=8),
    'Os': [np.nan, 25, 28, np.nan, 22, 18, 24, np.nan]
}
info=pd.DataFrame(data)
print(info)

info['Os'].fillna(info['Os'].mode()[0], inplace=True)
print(info)

#finding highest marks in different subjects
highest_Dsa=info.loc[info['Dsa'].idxmax(),['Name' , 'Dsa']]
highest_Maths=info.loc[info['Maths'].idxmax() , ['Maths' , 'Name']]
highest_Oops=info.loc[info['Oops'].idxmax(), ['Oops' , 'Name']]
highest_de=info.loc[info['DE'].idxmax(), ['DE', 'Name']]
highest_Os=info.loc[info['Os'].idxmax(),['Os','Name']]

print("The Highest Mark in Individual Subjects")
print(highest_Dsa)
print(highest_Maths)
print(highest_Oops)
print(highest_de)
print(highest_Os)

#finding Lowest marks in different subjects

lowest_Dsa=info.loc[info['Dsa'].idxmin(),['Name' , 'Dsa']]
lowest_Maths=info.loc[info['Maths'].idxmin() , ['Maths' , 'Name']]
lowest_Oops=info.loc[info['Oops'].idxmin(), ['Oops' , 'Name']]
lowest_de=info.loc[info['DE'].idxmin(), ['DE', 'Name']]
lowest_Os=info.loc[info['Os'].idxmin(),['Os','Name']]

print("The Lowest Mark in Individual Subjects")
print(lowest_Dsa)
print(lowest_Maths)
print(lowest_Oops)
print(lowest_de)
print(lowest_Os)

#finding average mark in every subject
Average_mark=info[['DE','Dsa' ,'Maths','Oops','Os']].mean()
print("Average mark in subjects:",Average_mark)

#fail below 15 marks

Failed_student=info[(info[['DE','Dsa','Maths','Oops','Os']]<15).any(axis=1)]
print("Students wo failed in atleast one subject",Failed_student['Name'])


#Top Performer of the Exam

info['totalmark']=info[['DE','Dsa','Maths','Oops','Os',]].sum(axis=1)

Topper=info.sort_values(by='totalmark', ascending=False)
print(Topper[['Name' , 'totalmark']])

