import pandas as pd
from IPython.display import display
import os

def readInputCsv(fileName: str) -> pd.DataFrame:
    """
    Read a CSV file into a pandas dataframe

    Inputs:
    fileName -- the input filename (including path)

    Returns an empty dataframe if it is not able to read the input file
    """

    df = pd.DataFrame()
    try:
        df = pd.read_csv(fileName)
        return df
    except:
        print("Something went wrong, check input csv")
        return df

# read the input file into a dataframe
df = readInputCsv('input.csv')
# display(df)

# create two lists from the dataframe
list1 = df['column1'].tolist()
list2 = df['column2'].tolist()

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