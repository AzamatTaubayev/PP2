l = ['a', 'b', 'c', 'd', 'e']

with open(r'C:\Users\Саламат\Desktop\PP2\week6\files_directories\list.txt', 'w') as file:
    for x in l:
        file.write(x)

f = open(r'C:\Users\Саламат\Desktop\PP2\week6\files_directories\list.txt')
print(f.read())