

import pandas as pd

def read_file(filePath: str, fileType: str, headerFlag: int = 0, excelSheet: str = 0) -> pd.DataFrame():
    """
    reads an input from the specified path 

    Parameters:
    fileName (string): the name of the file we want to read in
    headerFlag (int): the index of the row we want to use as heander (None for no header)

    Returns:
    a pandas dataframe (empty in the case of invalid input)
    """
    df = pd.DataFrame()

    try:
        if fileType == 'csv':
            df = pd.read_csv(filePath, header = headerFlag)
        elif fileType == 'json':
            df = pd.read_json(filePath)
        elif fileType == 'excel':
            df = pd.read_excel(filePath, header = headerFlag, sheet_name = excelSheet)

    except:
        print("Something went wrong, check input file name/path")
    
    return df