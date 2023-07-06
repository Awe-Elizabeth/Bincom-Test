from collections import Counter
from itertools import groupby



Monday = ['green', 'yellow', 'green', 'brown', 'blue', 'pink', 'blue', 'yellow', 'orange', 'cream', 'orange', 'red',
          'white', 'blue', 'blue', 'blue', 'blue', 'green'
          ]

Tuesday = ['arsh', 'brown', 'green', 'brown', 'blue', 'blue', 'blew', 'pink', 'pink', 'orange', 'orange', 'red', 'white', 'white',
           'blue', 'blue', 'blue'
           ]

Wednesday = ['green', 'yellow', 'green', 'brown', 'blue', 'pink', 'red', 'yellow', 'orange', 'red', 'blue', 'blue', 'white', 'blue', 'blue',
             'white', 'white'
            ]

Thursday = ['blue', 'blue', 'green', 'white', 'blue', 'brown', 'pink', 'yellow', 'orange', 'cream', 'orange', 'red', 'white',
            'blue',  'blue', 'blue', 'green'
            ]

Friday = ['green', 'white', 'green', 'brown', 'blue', 'blue', 'black', 'white', 'orange', 'red', 'red', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'white']


# w_colors = [x for lst in [Monday, Tuesday, Wednesday, Thursday, Friday] for x in lst]
w_colors = Monday + Tuesday + Wednesday + Thursday + Friday







# for item in med_colour:
#     new_list = []
#     new_list.append(med_colour[-1])
#     print (new_list)

# def max_occurence(seq=w_colors):
#     c = dict()
#     for item in seq:
#         c[item] = c.get(item, 0) + 1
#         return (max(c.items(), key=itemgetter(1)))

# max_occurence(seq=w_colors)






unique_colours = set(w_colors)


