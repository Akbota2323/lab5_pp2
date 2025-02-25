import re

txt = "The rain in Spain."
occurences = r'[ .,]'
x = re.sub(occurences, ":", txt)
print(x)