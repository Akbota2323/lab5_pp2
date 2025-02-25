import re

txt = "TheKazakhstan"
x = re.split("(?=[A-Z])", txt)
print(x)