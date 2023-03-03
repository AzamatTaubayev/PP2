n = int(input())
gen = (i*i for i in range(n))
for i in gen:
    print(i)