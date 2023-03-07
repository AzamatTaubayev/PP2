import re

with open(r"C://Users/Саламат/Desktop/PP2/week5/regex/receipt.txt", encoding="utf-8") as file:
    x = re.findall(r"\b[A-Z]\w+",file.read())
    for i in ((x)):
        for j in range(len(i)):
            print(i[j], end = ' ')