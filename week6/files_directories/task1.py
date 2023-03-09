import os

for root, directories, files in os.walk(r'C:\Users\Саламат\Desktop\PP2\week5'):
    print(root)
    for x in directories:
        print(x)
    for y in files:
        print(y)