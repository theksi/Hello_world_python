import re
# Regex library

string = " 'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)
# re.sub : Substitution
# 3 parameters  # --> 
    # pattern we want to match
    # What we want to replace with the match
    # The string we want to manipulate
    # Rules within regex are contained withing []
new = re.sub('[A-Z]','',string)
    # combination of multiple rules [A-Za-z]
    # if we want to remove spaces : [A-Z+" "]
string = string + " 6 299 - 560"
print ("######################################")
new = re.sub('[^0-9]','',string)
    # remove anything that's not number
print(new)

