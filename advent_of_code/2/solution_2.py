import pandas as pd
from IPython.display import display
from typing import List
from modules.read_file import read_file

debug = False

def get_sign(val: int) -> int:
    """
    Gets the sign of the input number

    Parameters:
    val (int): the value for which we want to find the sign

    Returns:
    the integer representation of the sign (-1 or 1)
    """

    return (val > 0) - (val < 0)

def remove_element(inputList: List[int], index:int = 0) -> List[int]:
    """
    Removes the element at index location

    Parameters:
    inputList: a list of elements
    index: the index of the element to remove from inputList

    Returns:
    A list with the element at index removed
    """
    returnList = inputList[:]
    del returnList[index]
    return returnList

def is_it_safe(row):
    """
    Determines if a dataframe row is 'safe' using the check_safety function. 
    Extention (dampening): If a row is demed 'unsafe' check if removing
    either element in the unsafe pair makes the row safe

    in this contxt a row is passed as a string which is then converted to a delimited list

    Parameters:
    row: a pandas dataframe row to be evaluated

    Returns:
    an integer representation of if the row is 'safe' (1 == safe, 0 == unsafe)
    commentary on why
    """

    rowList = List[int]
    rowList = [int(x) for x in row[0].split(" ")]

    if len(rowList) < 2:
        # too short, can't be safe
        return 0, 'List too short'
    
    safetyCheck = check_safety(rowList)

    if safetyCheck == -1:
        return 1, 'Safe as houses'
    elif safetyCheck == 1:
        # edge case, if it's not safe because of a sign flip removing the first 
        # element may resolve
        if(check_safety(remove_element(rowList, 0)) == -1):
            return 1, f"""Safe after removing the first element, edge case scenario"""

        # remove the left element of the problem pair and check again
        if(check_safety(remove_element(rowList, safetyCheck)) == -1):
            return 1, f"""Safe after removing left element at index {safetyCheck}"""

        # remove the right element of the problem pair and check again
        if(check_safety(remove_element(rowList, safetyCheck+1)) == -1):
            return 1, f"""Safe after removing right element at index {safetyCheck+1}"""
    
    else:

        # remove the left element of the problem pair and check again
        if(check_safety(remove_element(rowList, safetyCheck)) == -1):
            return 1, f"""Safe after removing left element at index {safetyCheck}"""

        # remove the right element of the problem pair and check again
        if(check_safety(remove_element(rowList, safetyCheck+1)) == -1):
            return 1, f"""Safe after removing right element at index {safetyCheck+1}"""
    
    # didn't get safe at any point, return 0
    return 0, 'No safe option even with dampening'
    
def check_safety(rowList: List[int]) -> int:
    """
    Determines if a dataframe row is 'safe' as defined by the following rules:
        - All entries in the row are either increasing or decreasing
        - Each entry is increasing or decreasing by a minimum of 1 and maximum of 3


    Parameters:
    rowList: a list representation of a row to be checked

    Returns:
    an integer representation of if the row is 'safe' or the index of the unsafe
    list item (-1 == safe)
    """

    # check initial condition to get sign (ascending or descending)
    initSign = get_sign(rowList[0] - rowList[1])
    
    if debug:
        print("initSign: " + str(initSign))

    if initSign == 0:
        # first two values are the same, not safe, exit
        return 0

    for i in range(len(rowList)-1):
        valDiff = rowList[i] - rowList[i+1]
        if debug:
            print('valDiff :' + str(valDiff))

        if (abs(valDiff) > 3 or abs(valDiff) < 1):
            # value difference is outside bounds, not safe, exit
            return i

        if get_sign(valDiff) != initSign:
            # values switch direction, not safe, exit
            return i
    
    return -1

# pull the input into a dataframe
df = read_file('./2/input.csv', 'csv', None)

# apply the is_it_safe function to all rows, appending the result and more info
df[[1,2]] = df.apply(is_it_safe, axis=1).apply(pd.Series)

# write df to csv (for validation)
df.to_csv('./2/output.csv')

# print the result of how many 'safe' rows there are
print(df[1].sum())