def removeWhitespace(s: str) -> str:
    """Removes whitespace from a string
    e.g. '  a b   c e  a \t  ' |-> 'a b c e a'"""
    return " ".join(s.split())

def removeComments(s: str) -> str:
    """Removes '#' comments from the end of a string by trimming after the first found hash.
    If no hash, return argument as-is
    e.g. 'abc#de#f' |-> 'abc'"""
    i = s.find("#")
    return s if i==-1 else s[:i]

