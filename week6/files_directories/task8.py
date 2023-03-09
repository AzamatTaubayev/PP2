import os

f = r'C:\Users\Саламат\Desktop\PP2\week6\files_directories\list.txt'

if os.path.exists(f):
    os.remove(f)
    print(f'File {os.path.basename(f)} deleted!!!')