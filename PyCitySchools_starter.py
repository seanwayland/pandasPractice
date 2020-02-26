#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:

# Dependencies and Setup
import pandas as pd

#from tabulate import tabulate

pd.set_option('display.width', 0)
# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

#print(school_data)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

# ## District Summary
# 
# * Calculate the total number of schools

numSchools = len(school_data.index)
print(numSchools)

# 
# * Calculate the total number of students

numStudents = len(student_data.index)
print(numStudents)
# * Calculate the total budget

totalBudget = school_data['budget'].sum()
print(totalBudget)

# * Calculate the average math score

totalMathScore = student_data['math_score'].sum()

print(totalMathScore)
averageMathScore = totalMathScore/numStudents
print(averageMathScore)
# 
# * Calculate the average reading score
#
totalReadingScore = student_data['reading_score'].sum()
print(totalReadingScore)
averageReadingScore = totalReadingScore/numStudents
print(averageReadingScore)

# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
#
overallPassingRate = (averageMathScore + averageReadingScore)/2
print(overallPassingRate)
# * Calculate the percentage of students with a passing math score (70 or greater)

mathSeventy = student_data[student_data['math_score'] >= 70]
mathSeventyAmt = len(mathSeventy)
print(mathSeventyAmt)
percentMathSeventy = mathSeventyAmt/numStudents*100
print(percentMathSeventy)


# * Calculate the percentage of students with a passing reading score (70 or greater)

readSeventy = student_data[student_data['reading_score'] >= 70]
readSeventyAmt = len(readSeventy)
print(readSeventyAmt)
percentReadSeventy = readSeventyAmt/numStudents*100
print(percentReadSeventy)
# * Create a dataframe to hold the above results
#

dfOne={'Total Schools' : [numSchools],'Total Students' :[numStudents],'Total Budget':[totalBudget], \
                                'Average Math Score' :[averageMathScore] ,'Average Reading Score' :[averageReadingScore], '% Passing Math' :[percentMathSeventy], '% Passing Reading' : [percentReadSeventy],'% Overall Passing Rate': [overallPassingRate]}
# * Optional: give the displayed data cleaner formatting

dfOne = pd.DataFrame(dfOne)
dfOne.style.hide_index()



# * Optional: give the displayed data cleaner formatting
#pd.options.display.float_format = '{0:,.2f}'.format
#pd.options.display.integer_format = '{:, .2f}'.format

#dfOne[2][0] = dfOne[2][0].map('${:,.2f}'.format)
dfOne['Total Budget']=dfOne['Total Budget'].apply(lambda x: "${:,.2f}".format(x))
dfOne['Total Students']=dfOne['Total Students'].apply(lambda x: "{:,}".format(x))


print(dfOne)


# In[11]:





# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:

#print(school_data)

#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget

schoolOverview = school_data.copy()
#print(schoolOverview.head())



#print(schoolOverview.head())

# add per student budget to table

schoolOverview['per student budget'] = schoolOverview['budget']/schoolOverview['size']

#   * Average Math Score

# group student table by school
# total


#schoolMeans = pd.DataFrame(school_data_complete.groupby(["school_name"]).mean())
eachSchool = pd.DataFrame(school_data_complete.groupby(["school_name"]))
schoolMeans = school_data_complete.groupby(["school_name"]).mean()
pd.set_option('display.max_colwidth', 0)
SchoolAvgMath = schoolMeans['math_score']
SchoolAvgRead = schoolMeans['reading_score']
print(schoolMeans)
print(eachSchool)
print(SchoolAvgMath)



#print("cc")
#dfThree = dfTwo("math_score").mean()
#print(dfThree)

#schoolOverview['average Math Score ']

#print(schoolOverview)
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[13]:





# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[14]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[15]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[16]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[19]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:





# In[ ]:




