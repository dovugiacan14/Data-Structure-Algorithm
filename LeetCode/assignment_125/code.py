def is_palindorme(s):
    if not s: 
        return True 
    s = s.replace(',',"").replace(" ", "").replace(":", "").replace('.', "").replace("@", "").replace("#", "").replace("_", "")
    s = s.lower()
    reversed_text = s[::-1]
    if s == reversed_text:
        return True 
    return False

import re
def is_palindorme(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]
