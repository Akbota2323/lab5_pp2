import re

txt = "TheKazakhstan"
x = re.sub("(?<!^)(?=[A-Z])"," ", txt)
print(x)
