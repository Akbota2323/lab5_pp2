import re
txt = "abc_def ghi_jkl"
x = re.findall("[a-z]+_[a-z]+",txt)
print(x)
