import re 
def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return re.match(pattern, s.strip()) is not None
