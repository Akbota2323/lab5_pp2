import re
txt = "Akbota aBYLKAKOVA Abylkakova"
x = re.findall("[A-Z][a-z]+",txt)
print(x)