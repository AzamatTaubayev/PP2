import re

file = open('C:/Users/Саламат/Desktop/PP2/week5/regex/receipt.txt', "r", encoding = "UTF8")

result = re.findall(".*a.*b.*b.*b?.*", file.read())
print(result)