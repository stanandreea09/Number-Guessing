import random

x = random.randint(1, 100)
v = True
while(v):
    y = int(input("Try to guess:\n"))
    if(y < x):
        print("Your number is too small :( ")
    elif(y>x):
        print("Your number is too big :( ")
    else:
        v = False
print("You are lucky.")

