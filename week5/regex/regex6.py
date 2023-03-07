import re

file = open("C://Users/Саламат/Desktop/PP2/week5/regex/receipt.txt", "r")

result = re.sub("[ ,.]",":", file.read())

print(result)