
# coding: utf-8

# In[56]:

# The Algebra data set is a csv file, comprised of 999 student grades. 
# The file shows for each student: First and Last Names,Gender, Grade and Hours of Study.
# Python for Data-Analytics is used to perform simple analysis of the dataset.


# In[57]:

# Import Libraries
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import sys

# Enable inline plotting
get_ipython().magic(u'matplotlib inline')


# In[58]:

# Location of file
Location = "C:\\Users\\Matthew\\Desktop\\datasets\\algebradata.csv"


# In[59]:

# Loading data from csv file
df = pd.read_csv(Location)


# In[60]:

# Create a column 'is Failing' to deduce students with passing grades
df['is Failing'] = np.where(df['Grade']>'C', 'yes', 'no')


# In[61]:

df.tail()


# In[62]:

# The response "no" to 'is failing' = number of students with passing grades(A,B or C)
# The total number of students passing is 691/999
# % of students passing = 691/999 * 100 = 
df.loc[df['is Failing']=='no'].count()


# In[63]:

def score_to_numeric(x):
    if x=='F':
        return 1
    if x=='M':
        return 0


# In[64]:

# Applying a numeric score to Gender for easier analysis:
df['Gender_val'] = df['Gender'].apply(score_to_numeric)


# In[65]:

df.tail()


# In[66]:

# Creating and applying numeric score to passing grade
# passing Grade returns 1 and failing returns 0


# In[67]:

def score_to_numeric(x):
    if x=='no':
        return 1
    if x=='yes':
        return 0


# In[68]:

df['Passing_val'] = df['is Failing'].apply(score_to_numeric)


# In[69]:

df.tail()


# In[70]:

# Results below shows that:
# average hour of study for all student is 15.15 hours
# that 69.1% of students had passing grades
# there were no missing values
df.describe()


# In[71]:

# Data also confirms that 69.1% of students had passing grades
temp1 = df['Passing_val'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Gender',index=['Passing_val'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print 'Frequency Table for Passing_val:' 
print temp1


# In[72]:

# Box-plot shows almost equal amounts of men to women
df.boxplot(column='Passing_val', by = 'Gender_val')


# In[73]:

# To determine Average hours of study for students with passing Grade:
# The average hours of study for students with passing grade is 16.3 hours.
df.loc[df['Passing_val']==1]['Hours of Study'].mean()


# In[74]:

# Hours of study showed a stronger correlation with passing grade than did Gender
df.corr()


# In[75]:

# 
df.loc[df['Gender_val']==1]['Passing_val'].count()


# In[76]:

# results of Histogram shows number of Female and Males with passing grades
# 0 represents Failing grades and 1 represents passing grades
df.hist(column="Passing_val", by="Gender")


# In[77]:

# Of the 518 women, approximately 380 had passing grade
# 380/518 *100 = ~73.4% of women had passing grades


# In[78]:

# Conclusion
# 69.1% of students had passing grades
# 73.4% of women had passing grades
# The average hour of study for all students is 15.5 hours
# The average hour of study for students with passing grade is 16.3 hours


# In[ ]:



