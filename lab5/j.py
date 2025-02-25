import re

txt = "snaleCaseCamelCase"
x = re.sub(r"(?<!^)(?=[A-Z])", "_", txt)
print(x)