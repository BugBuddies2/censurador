import re

def filter_text(txt, words, rep="***"):
    if not txt or not words:
        return txt
    p = '|'.join(r'\b' + re.escape(w) + r'\b' for w in words)
    return re.sub(p, lambda x: rep, txt, flags=re.IGNORECASE) 