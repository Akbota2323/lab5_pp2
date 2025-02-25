import re
txt = "abbbbb"
x = re.search("^ab*$",txt)
if x:
    print("Yes!")
else:
    print("No")