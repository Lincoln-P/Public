import re

# get the input text file
f = open('./3/input.txt', 'r')

# remove any newline characters
# note: not sure how we should be treating valid mul(X,Y) strings
# across newline breaks, for the purpose of this exercise we
# will treat them as valid
inputText = f.read().replace('\n',"")

# find locations of do() and don't() functions
controls = re.finditer(r"do\(\)|don\'t\(\)", inputText)

# we can use those control locations to define substrings to get only the mul
# activities encapsulated in 'do' blocks
muls = []

# the iterator is the 'breaks' in the string, we need to ensure we also capture
# the start and end when we want to make substrings
# note: assume the first block is a 'do' block
prev = 0
prevControl = 'do()'

# iterate
for obj in controls:
    if prevControl == 'do()':
        muls.append(re.findall(r"mul\(\d+\,\d+\)", inputText[prev:obj.span()[0]]))

    prev = obj.span()[1]
    prevControl = obj.group()

# catch the final run
if prevControl == 'do()':
    muls.append(re.findall(r"mul\(\d+\,\d+\)", inputText[prev:len(inputText)]))


# flatten the list of lists
muls = [x for xs in muls for x in xs]

# we know the format is going to be mul(x,y) so we can just concatenate
# the list and extract the digits
mulString = ''.join(muls)
muls = re.findall(r"\d+", mulString)

# now multiply in sets of 2
total = 0
for i in range(0, len(muls), 2):
    total += (int(muls[i]) * int(muls[i + 1]))

print(total)