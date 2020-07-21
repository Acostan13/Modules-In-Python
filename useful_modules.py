from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah thinking about python'
print(Counter(li))  # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(Counter(sentence))  # Counter({'h': 4, ' ': 4, 'b': 3, 'a': 3, 't': 3, 'n': 3, 'l': 2, 'i': 2, 'o': 2, 'k': 1, 'g': 1, 'u': 1, 'p': 1, 'y': 1})


dictionary = defaultdict(int, {'a': 1, 'b': 2})
print(int())  # 0

dictionary2 = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary2['c'])  # 5


d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

d3= OrderedDict()
d3['b'] = 2
d3['a'] = 1

print(d2 == d)  # True
print(d3 == d2)  # False

print(datetime.time())  # 00:00:00
print(datetime.time(5, 45, 2))  # 05:45:02
print(datetime.date.today())  # 2020-07-19 - Today's date

arr = array('i', [1, 2, 3])  # slightly better performing then lists
print(arr[0])  # 1
