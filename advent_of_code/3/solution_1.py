import re

# get the input text file
f = open('./3/input.txt', 'r')

# remove any newline characters
# note: not sure how we should be treating valid mul(X,Y) strings
#       across newline breaks, for the purpose of this exercise we
#       will treat them as valid
inputText = f.read().replace('\n',"")

# split the string into a list of matches based on the pattern
muls = []
muls = re.findall("mul\(\d+\,\d+\)", inputText)


# we know the format is going to be mul(x,y) so we can just concatenate
# the list and extract the digits
mulString = ''.join(muls)
muls = re.findall("\d+", mulString)

# now multiply in sets of 2
total = 0
for i in range(0, len(muls), 2):
    total += (int(muls[i]) * int(muls[i + 1]))

print(total)