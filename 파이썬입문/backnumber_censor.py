
data = """ 
lee = 990225-1232322
kim = 971003-2382411
"""

import re
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
