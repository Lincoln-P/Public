import pandas as pd
from IPython.display import display
from modules.read_file import read_file


# read the input file into a dataframe
df = read_file('./1/input.csv', 'csv')


# let's do some data engineering

"""
SQL representation

with leftSet as (
    select column1 from df
),
rightSet as (
    select disctinct column2, count(1) as count
    from df
    group by column2
),
combinedSet as (
    select ls.column1, rs.count
    from leftSet ls
    join rightSet rs ON ls.column1 = rs.column2 AND rs.column2 is not null
)

select sum(multiple) from (
    select column1, count, (column1 * count) as multiple
    from combinedSet
)

"""

# pandas time

# get the left set
leftSet = df[['column1']]

# get the right set and count of values in it 
rightSet = df[['column2']]
rightSet['count'] = rightSet.groupby('column2')['column2'].transform('count')
rightSet = rightSet.drop_duplicates()

# combine the sets
combinedSet = leftSet.merge(rightSet, left_on='column1', right_on='column2')
# get rid of unnecessary columns
combinedSet = combinedSet[['column1', 'count']]

# add a multiplication column
combinedSet['multiple'] = combinedSet['column1'] * combinedSet['count']

# get the sum of the multiple column
print(combinedSet['multiple'].sum())
