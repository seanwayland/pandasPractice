# Dependencies and Setup
import pandas as pd

# from tabulate import tabulate

pd.set_option('display.width', 0)
# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


#print(student_data.head())



# ## District Summary
#
# * Calculate the total number of schools

numSchools = len(school_data.index)
#print(numSchools)

#
# * Calculate the total number of students

numStudents = len(student_data.index)
#print(numStudents)
# * Calculate the total budget

# * Calculate the total budget

totalBudget = school_data['budget'].sum()
#print(totalBudget)

# * Calculate the average math score

totalMathScore = student_data['math_score'].sum()

#print(totalMathScore)
averageMathScore = totalMathScore / numStudents
#print(averageMathScore)
#
# * Calculate the average reading score
#
totalReadingScore = student_data['reading_score'].sum()
#print(totalReadingScore)
averageReadingScore = totalReadingScore / numStudents
#print(averageReadingScore)

# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
#
overallPassingRate = (averageMathScore + averageReadingScore) / 2
#print(overallPassingRate)
# * Calculate the percentage of students with a passing math score (70 or greater)

mathSeventy = student_data[student_data['math_score'] >= 70]
mathSeventyAmt = len(mathSeventy)
#print(mathSeventyAmt)
percentMathSeventy = mathSeventyAmt / numStudents * 100
#print(percentMathSeventy)

# * Calculate the percentage of students with a passing reading score (70 or greater)

readSeventy = student_data[student_data['reading_score'] >= 70]
readSeventyAmt = len(readSeventy)
#print(readSeventyAmt)
percentReadSeventy = readSeventyAmt / numStudents * 100
#print(percentReadSeventy)


# * Create a dataframe to hold the above results
#

dfOne = {'Total Schools': [numSchools], 'Total Students': [numStudents], 'Total Budget': [totalBudget], \
         'Average Math Score': [averageMathScore], 'Average Reading Score': [averageReadingScore],
         '% Passing Math': [percentMathSeventy], '% Passing Reading': [percentReadSeventy],
         '% Overall Passing Rate': [overallPassingRate]}
# * Optional: give the displayed data cleaner formatting

dfOne = pd.DataFrame(dfOne)
dfOne.style.hide_index()

# * Optional: give the displayed data cleaner formatting
# pd.options.display.float_format = '{0:,.2f}'.format
# pd.options.display.integer_format = '{:, .2f}'.format

# dfOne[2][0] = dfOne[2][0].map('${:,.2f}'.format)
dfOne['Total Budget'] = dfOne['Total Budget'].apply(lambda x: "${:,.2f}".format(x))
dfOne['Total Students'] = dfOne['Total Students'].apply(lambda x: "{:,}".format(x))

#print(dfOne)


sdc = school_data_complete.copy()
sdcg = sdc.groupby('school_name')
schoolMeans = sdcg.mean()
#print(schoolMeans)
#Average Math Score
#Average Reading Score

#print(school_data)
sdm = pd.merge(school_data, schoolMeans, on = "school_name")

#['Student ID', 'School ID_y', 'size_y', 'budget_y']
del sdm['Student ID']
del sdm['School ID_y']
del sdm['size_y']
del sdm['budget_y']

#sdm.rename(columns={"School ID_x": "School ID", "size_x": "size", "budget_x" : "budget", "reading_score" : "average reading score ", "math_score" : "average reading score "})
sdm=sdm.rename(columns = {'School ID_x':'School Id'})
sdm=sdm.rename(columns = {'size_x':'size'})
sdm=sdm.rename(columns = {'budget_x':'budget'})
sdm=sdm.rename(columns = {'reading_score':'avg read score'})
sdm=sdm.rename(columns = {'math_score':'avg math score'})

sdcg = pd.DataFrame(sdcg)
pd.set_option('display.max_colwidth', 0)
#print(sdcg.head())

#Select students from large data set that scored greater than 70
studentsPassingReading = student_data[student_data['reading_score'] >= 70]
studentsPassingMath = student_data[student_data['math_score'] >= 70]


#Count of students passing reading at each school
passingReadingTable =studentsPassingReading.groupby(['school_name'])['reading_score'].count().reset_index()
passingReadingTable.rename({'reading_score':'reading_count>70'},axis=1,inplace=True)

#print(passingReadingTable)
#Count of students passing math at each school
passingMathTable = studentsPassingMath.groupby(['school_name'])['math_score'].count().reset_index()
passingMathTable.rename({'math_score':'math_count>70'},axis=1,inplace=True)
#print(passingMathTable)

sdm = pd.merge(sdm, passingReadingTable, on = "school_name")
sdm = pd.merge(sdm, passingMathTable, on = "school_name")



sdm['% reading >70'] = sdm['reading_count>70']/sdm['size']*100
sdm['% math >70'] = sdm['math_count>70']/sdm['size']*100


sdm['% overall passing'] = (sdm['% reading >70'] + sdm['% math >70'])/2

#print(sdm)




'''


Create an overview table that summarizes key metrics about each school, including:
School Name
School Type
Total Students
Total School Budget
Per Student Budget
Average Math Score
Average Reading Score
% Passing Math
% Passing Reading
Overall Passing Rate (Average of the above two)
'''




topFiveSchools = sdm.sort_values(by=['% overall passing'],ascending=False).head(5)
#print(topFiveSchools)

'''
Reading Scores by Grade
Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
'''

grade =  school_data_complete.groupby(['school_name', 'grade']).agg({'reading_score': ['mean']})
print(grade)

#print(grade)

'''
Scores by School Spending
Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
Average Math Score
Average Reading Score
% Passing Math
% Passing Reading
Overall Passing Rate (Average of the above two)
 
'''
#print(sdm)
# add column budget/size
sdm['per student budget'] = sdm['budget']/sdm['size']
#print(sdm)

# bins 580 , 600 , 620 , 640
bins = [577, 600, 620, 640, 660]

sdm['spending summary'] = pd.cut(sdm["per student budget"], bins, labels=['577-600', '600-620', '620-640', '640-660'])

sdm2 = sdm.copy()
sdm2 = sdm2.sort_values(by=['spending summary'],ascending=False)
print(sdm2)
