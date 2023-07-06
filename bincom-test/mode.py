from index import w_colors
from collections import Counter

def max_colour ():
    c = Counter(w_colors)
    return(c.most_common(1))

max_colour()