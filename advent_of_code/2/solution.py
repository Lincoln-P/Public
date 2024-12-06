import pandas as pd
from IPython.display import display
from typing import List

debug = False

def read_input_csv(fileName: str, headerFlag: int = 1) -> pd.DataFrame():
    """
    reads an input csv from the local (immediate) directory 

    Parameters:
    fileName (string): the name of the file we want to read in
    headerFlag (int): the index of the row we want to use as heander (None for no header)

    Returns:
    a pandas dataframe (empty in the case of invalid input)
    """
    df = pd.DataFrame()

    try:
        df = pd.read_csv(fileName, header=headerFlag)

    except:
        print("Something went wrong, check input file name/path")
    
    return df

def get_sign(val: int) -> int:
    """
    Gets the sign of the input number

    Parameters:
    val (int): the value for which we want to find the sign

    Returns:
    the integer representation of the sign (-1 or 1)
    """

    return (val > 0) - (val < 0)

def is_it_safe(row):
    """
    Determines if a dataframe row is 'safe' as defined by the following rules:
        - All entries in the row are either increasing or decreasing
        - Each entry is increasing or decreasing by a minimum of 1 and maximum of 3

    in this contxt a row is passed as a string which is then converted to a delimited list

    Parameters:
    row: a pandas dataframe row to be evaluated

    Returns:
    an integer representation of if the row is 'safe' (1 == safe, 0 == unsafe)
    """
    rowList = List[int]
    rowList = [int(x) for x in row[0].split(" ")]
    if debug:
        print(rowList)

    # ensure the length of the row is at least 2
    if debug:
        print("rowLength: " + str(len(rowList)))

    if len(rowList) < 2:
        # too short, can't be safe, exit
        return 0, 'Too short'

    # check initial condition to get sign (ascending or descending)
    initSign = get_sign(rowList[0] - rowList[1])
    
    if debug:
        print("initSign: " + str(initSign))

    if initSign == 0:
        # first two values are the same, not safe, exit
        return 0, f"""Val diff for {rowList[0]} and {rowList[1]} is not amenable"""

    for i in range(len(rowList)-1):
        valDiff = rowList[i] - rowList[i+1]
        if debug:
            print('valDiff :' + str(valDiff))

        if (abs(valDiff) > 3 or abs(valDiff) < 1):
            # value difference is outside bounds, not safe, exit
            return 0, f"""Val diff for {rowList[i]} and {rowList[i+1]} is not amenable"""

        if get_sign(valDiff) != initSign:
            # values switch direction, not safe, exit
            return 0, f"""Val direction switches, {rowList[i-1]},{rowList[i]},{rowList[i+1]}"""
        
    return 1, 'Checks out'
        
# pull the input into a dataframe
df = read_input_csv('input.csv', None)

# apply the is_it_safe function to all rows, appending the result and more info
df[[1,2]] = df.apply(is_it_safe, axis=1).apply(pd.Series)

# write df to csv (for validation)
df.to_csv('output.csv')

# print the result of how many 'safe' rows there are
print(df[1].sum())