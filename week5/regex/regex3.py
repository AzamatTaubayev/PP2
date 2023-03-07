import re
file = open('C:/Users/Саламат/Desktop/PP2/week5/regex/receipt.txt', "r", encoding = "UTF8")

result = re.findall("[a-z]+_[a-z]+", file.read())
print(result)