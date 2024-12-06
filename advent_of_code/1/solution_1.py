import pandas as pd
from IPython.display import display
import os
from modules.read_file import read_file


# read the input file into a dataframe
df = read_file('./1/input.csv', 'csv')
# display(df)

# create two lists from the dataframe
list1 = df["column1"].tolist()
list2 = df["column2"].tolist()

# sort the lists
list1.sort()
list2.sort()

# holding variable to store the return value as we iterate through the lists
diffCount = 0

# iterate through the lists and add the difference (absolute) to the holding variable
for i in range(len(list1)):
    diffCount += abs(list1[i] - list2[i])

# display the output
print(diffCount)
