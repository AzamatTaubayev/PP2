import re

with open(r"C://Users/Саламат/Desktop/PP2/week5/regex/receipt.txt", encoding='utf-8') as file:
    result = re.sub(r'_([a-z])', lambda match : match.group(1).upper(), file.read())
    print(result)