import random
print("Hello! What is your name?")
name = input()
print("Well,", name,"I am thinking of a number between 1 and 20. Take a guess.")
l = 1
cnt = 0
a = random.randint(1,20)
while l>0:
    n = int(input())
    cnt+=1
    if n>a:
        print("""Your guess is too high.
Take a guess.""")
    elif n<a:
        print("""Your guess is too low.
Take a guess.""")
    else:
        print("Good job", name,"you guessed my number in", cnt,"guesses.") 
        break

