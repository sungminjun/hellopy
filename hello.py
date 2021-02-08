import this

import re
import sys
import pprint

# list comprehension
str1 = 'foobarbaz'
strls = [str1[i:i+2].lower() for i in range(len(str1) - 1) if re.findall('[a-z]{2}', str1[i:i+2].lower())]
pprint.pprint(locals())


import re
import sys
import pprint

str1 = 'foobarbazchocobar'
slice = 4
search_pat = '[a-z]{{{0}}}'.format(slice)
search_pat
strls = [
    str1[i:i+slice].lower() for i in range(len(str1) - (slice-1)) 
    if re.findall(search_pat, str1[i:i+(slice)].lower())
]
pprint.pprint(locals())
strls

# another way
strls = [
    str1[i:i+2].lower() for i in range(len(str1)-1)
    if re.findall('[a-z]{2}', str1[i:i+2].lower())
]
strls

# mb c-like or java-like?
strls = []
for i in range(len(str1) -1):
    if re.findall('[a-z]{2}', str1[i:i+2].lower()):
        strls.append(str1[i:i+2].lower())
strls

