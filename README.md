# Algebradata
Assignment 1

# The Algebra data set is a csv file, comprised of 999 student grades. 
# The file shows for each student: First and Last Names,Gender, Grade and Hours of Study.
# Python for Data-Analytics is used to perform simple analysis of the dataset.
In [57]:
# Import Libraries
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import sys

# Enable inline plotting
%matplotlib inline
In [58]:
# Location of file
Location = "C:\\Users\\Matthew\\Desktop\\datasets\\algebradata.csv"
In [59]:
# Loading data from csv file
df = pd.read_csv(Location)
In [60]:
# Create a column 'is Failing' to deduce students with passing grades
df['is Failing'] = np.where(df['Grade']>'C', 'yes', 'no')
In [61]:
df.tail()
Out[61]:
Fname	Lname	Gender	Grade	Hours of Study	is Failing
994	Harold	Looner	M	D	11	yes
995	Paula	Moore	F	C	6	no
996	Martin	Franklin	M	C	25	no
997	Nicole	Henderson	F	A	20	no
998	Veronica	Harrison	F	D	21	yes
In [62]:
# The response "no" to 'is failing' = number of students with passing grades(A,B or C)
# The total number of students passing is 691/999
# % of students passing = 691/999 * 100 = 
df.loc[df['is Failing']=='no'].count()
Out[62]:
Fname             691
Lname             691
Gender            691
Grade             691
Hours of Study    691
is Failing        691
dtype: int64
In [63]:
def score_to_numeric(x):
    if x=='F':
        return 1
    if x=='M':
        return 0
In [64]:
# Applying a numeric score to Gender for easier analysis:
df['Gender_val'] = df['Gender'].apply(score_to_numeric)
In [65]:
df.tail()
Out[65]:
Fname	Lname	Gender	Grade	Hours of Study	is Failing	Gender_val
994	Harold	Looner	M	D	11	yes	0
995	Paula	Moore	F	C	6	no	1
996	Martin	Franklin	M	C	25	no	0
997	Nicole	Henderson	F	A	20	no	1
998	Veronica	Harrison	F	D	21	yes	1
In [66]:
# Creating and applying numeric score to passing grade
# passing Grade returns 1 and failing returns 0
In [67]:
def score_to_numeric(x):
    if x=='no':
        return 1
    if x=='yes':
        return 0
In [68]:
df['Passing_val'] = df['is Failing'].apply(score_to_numeric)
In [69]:
df.tail()
Out[69]:
Fname	Lname	Gender	Grade	Hours of Study	is Failing	Gender_val	Passing_val
994	Harold	Looner	M	D	11	yes	0	0
995	Paula	Moore	F	C	6	no	1	1
996	Martin	Franklin	M	C	25	no	0	1
997	Nicole	Henderson	F	A	20	no	1	1
998	Veronica	Harrison	F	D	21	yes	1	0
In [70]:
# Results below shows that:
# average hour of study for all student is 15.15 hours
# that 69.1% of students had passing grades
# there were no missing values
df.describe()
Out[70]:
Hours of Study	Gender_val	Passing_val
count	999.000000	999.000000	999.000000
mean	15.115115	0.518519	0.691692
std	8.991187	0.499907	0.462026
min	0.000000	0.000000	0.000000
25%	7.000000	0.000000	0.000000
50%	15.000000	1.000000	1.000000
75%	23.000000	1.000000	1.000000
max	30.000000	1.000000	1.000000
In [71]:
# Data also confirms that 69.1% of students had passing grades
temp1 = df['Passing_val'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Gender',index=['Passing_val'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print 'Frequency Table for Passing_val:' 
print temp1
Frequency Table for Passing_val:
0    308
1    691
Name: Passing_val, dtype: int64
In [72]:
# Box-plot shows almost equal amounts of men to women
df.boxplot(column='Passing_val', by = 'Gender_val')
Out[72]:
<matplotlib.axes._subplots.AxesSubplot at 0xd45add8>

In [73]:
# To determine Average hours of study for students with passing Grade:
# The average hours of study for students with passing grade is 16.3 hours.
df.loc[df['Passing_val']==1]['Hours of Study'].mean()
Out[73]:
16.29811866859624
In [74]:
# Hours of study showed a stronger correlation with passing grade than did Gender
df.corr()
Out[74]:
Hours of Study	Gender_val	Passing_val
Hours of Study	1.000000	0.063617	0.197174
Gender_val	0.063617	1.000000	0.098494
Passing_val	0.197174	0.098494	1.000000
In [75]:
# 
df.loc[df['Gender_val']==1]['Passing_val'].count()
Out[75]:
518
In [76]:
# results of Histogram shows number of Female and Males with passing grades
# 0 represents Failing grades and 1 represents passing grades
df.hist(column="Passing_val", by="Gender")
Out[76]:
array([<matplotlib.axes._subplots.AxesSubplot object at 0x000000000D4B5320>,
       <matplotlib.axes._subplots.AxesSubplot object at 0x000000000D70A208>], dtype=object)

In [77]:
# Of the 518 women, approximately 380 had passing grade
# 380/518 *100 = ~73.4% of women had passing grades
In [78]:
# Conclusion
# 69.1% of students had passing grades
# 73.4% of women had passing grades
# The average hour of study for all students is 15.5 hours
# The average hour of study for students with passing grade is 16.3 hours
In [ ]:
 
