def myfunc(n):
  return lambda a : a * n
n = int(input())
mydoubler = myfunc(n)
mytripler = myfunc(n)
a = int(input())
b = int(input())
print(mydoubler(b))
print(mytripler(a))