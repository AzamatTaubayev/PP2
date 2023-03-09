import os

f = r'C:\Users\Саламат\Desktop\PP2\week5\regex\receipt.txt'

if os.path.exists(f):
    if os.path.isdir(f):
        print(os.path.dirname(f))
    else:
        print(os.path.basename(f))
else:
    print("I could not find directory like this")