import re

txt = "snale_case_camel_case"
occurences = r'[_]'
x = re.sub(occurences, "", txt)
print(x)