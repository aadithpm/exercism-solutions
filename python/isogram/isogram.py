from re import sub
def is_isogram(string):
    string = sub("[^A-Za-z]", "", string)
    return len(string) == len(set(string.lower()))
