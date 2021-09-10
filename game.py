import random
n = random.randint(0,2)


z = input("Guess the number")

if z == n:
    print("You guessed right!")
elif z > n:
    print("Lower.")
elif z < n:
    print("Higher.")