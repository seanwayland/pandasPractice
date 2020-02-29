import pandas as pd

# mathSeventy = student_data[student_data['math_score'] >= 70]

#declare a dict of lists version of the data
# note the length of each array has to the same otherwise the compiler will complain
dataDictOfList = {'team': ["A", "B", "C", "C", "D", "D", "E"], 'score': [1, 2, 3, 4, 5, 6, 7]}
dictListDataFrame = pd.DataFrame(dataDictOfList)
print("dictListDataFrame")
print(dictListDataFrame)
#sum of score for each team
teamTotals = dictListDataFrame.groupby('team').sum()
print("sum of score for each team")
print(teamTotals)
#only teams whose sum is greater than 3
print("teams whose sum is greater than 3")
totalGreaterThanThree = teamTotals[teamTotals['score'] > 3]
print(totalGreaterThanThree)
#how many times did each team score more than 3
gamesAboveThree = dictListDataFrame[dictListDataFrame['score'] > 3]
gamesAboveThree = gamesAboveThree.groupby('team').count()
print("how many times each team scored more than 3 ")
print(gamesAboveThree)

#declare a list of list version of the data
# note the number of members of each array is the number of columns
# the number of arrays is the number of rows
ListofListCols = ['team', 'score']
dataListofList = [["A", 1], ["B", 2], ["C", 3], ["C", 4], ["D", 5], ["D", 6], ["E", 7], ]
listListDataFrame = pd.DataFrame(dataListofList, columns=ListofListCols)
print("list of lists data frame")
print(listListDataFrame)

LLtotals = listListDataFrame.groupby('team').sum()

#only teams whose sum is greater than 3

LLGreaterThanThree = LLtotals[LLtotals['score'] > 3]

print("teams whose sum is greater than 3 from list of lists ")
print(LLGreaterThanThree)
