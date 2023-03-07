import re

with open(r"C://Users/Саламат/Desktop/PP2/week5/regex/receipt.txt", encoding="utf-8") as file:
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', file.read()).lower()
    print(result)