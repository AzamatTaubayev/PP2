with open(r'C:\Users\Саламат\Desktop\PP2\week6\files_directories\somedoc.txt', 'r') as to_read:
    with open('B.txt', 'w') as write:
        for x in to_read.read():
            write.write(x)