import re

with open(r"C://Users/Саламат/Desktop/PP2/week5/regex/receipt.txt", encoding="utf-8") as file:
    result = re.findall(r'[A-Z][^A-Z]*', file.read() )
    print(result)