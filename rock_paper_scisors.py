import random


def gamewin(comp, a):
    if comp == "r":
        if a == "p":
            return True
        else:
            return False
    elif comp == "p":
        if a == "s":
            return True
        else:
            return False
    elif comp == "s":
        if a == "r":
            return True
        else:
            return False


print("1st computers turn : ")
a = input("\nyour turn choose (r)rock, (p)paper, (s)scisors : ")
randno = random.randint(1, 3)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
elif randno == 3:
    comp = "s"

if comp == a:
    print("\nits a Tie!")
else:
    b = gamewin(comp, a)
    if b:
        print("\nyou Win!")
    else:
        print("\nyou Lose!")
print("\ncomp chose :  "+comp.upper())
print("\nyou chose  :  "+a.upper())
