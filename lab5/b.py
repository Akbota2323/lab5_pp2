import re
txt = "abbbb"
x = re.search("^ab{2,3}$",txt)
if x:
    print("Yes!")
else:
    print("No")
