import re
import sys
from collections import OrderedDict

str=sys.stdin.read()

str = str.strip().lower().replace('\n',' ')
dict1=OrderedDict()
for s in str.split("."):
	token=list(w for w in s.split(" ") if w is not '')
	count=0
	while count <= len(token)-3:
		tup1 = (token[count],token[count+1],token[count+2]);
		if tup1 in dict1.keys():
			dict1[tup1] += 1;
		else:
			dict1 = OrderedDict(dict1.items() + {tup1:1}.items())
		count+=1
print (' '.join(max(dict1, key=dict1.get)))
