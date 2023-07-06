from index import w_colors
from collections import Counter

def med_colour ():
    c = Counter(w_colors)
    count = len(c)
    med = int(count/2)
    com = c.most_common()
    print(com[med - 1])

med_colour()


    