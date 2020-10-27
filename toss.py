'''import random
choose=["Heads","Tails"]
coin=random.choice(choose)
toss=input("Heads or Tails:")

if coin == toss:
    print("its",coin,"You won the toss :)")
else:
    print("its",coin,"You loose the toss :(")'''


    
import random
coin=random.randint(0,1)
toss=input("Heads or Tails:")
if toss in ["Heads","heads"]:
    toss = 0
    if coin==toss:
        print("You won the toss :)")
    else:
        print("You loose the toss :(")

elif toss in ["Tails","tails"]:
    toss = 1
    if coin==toss:
        print("You won the toss :)")
    else:
        print("You loose the toss :(")