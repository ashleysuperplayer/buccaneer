def removeWhitespace(string):
    return " ".join(string.split())

def removeComments(string):
    i = string.find("#")
    if i == -1:
        return string
    else:
        return string[:i]
