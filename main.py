score_u = 0
score_c = 0

import random
n = ["s","p","r"]


print('''welcome to the game''')

rnd = int(input("How many rounds you want to play? :"))


for i in range(rnd):
    print(f"round {i+1} begans!! ")
    comp = random.choice(n)
    user = input('''choose:  r for rock🗿" 
         p for paper📜
         s for scissor🔪    :''')
    if comp == user:
        print("\n\n you choose the same as me😐\n\n")
        continue

    elif comp == "s" and user == "r":
        score_u +=1
        print("\n\nI choose scissor🔪!!! ahh you got me😒\n\n")

    elif comp == "s" and user == "p":
        score_c +=1
        print("\n\nI choose scissor🔪!!! .gotcha😉\n\n")

    elif comp == "p" and user == "s":
        score_u +=1
        print("\n\nI choose paper📜!!!   ahh you got me😒\n\n")

    elif comp == "p" and user == "r":
        score_c +=1
        print("\n\nI choose paper📜!!!   you got cooked😭😂\n\n")

    elif comp == "r" and user == "p":
        score_u +=1
        print("\n\nI choose Rockkk🗿!!!  ahh you got me😒\n\n")

    elif comp == "r" and user == "s":
        score_c +=1
        print("\n\nI choose Rockkk🗿!!!  cooked you 😂\n\n")

if score_u > score_c:
    print("\n\nYOU WON!!!🏆\n\n")
elif score_c > score_u:
    print("\n\nYou fumbled hard 👎🏻\n\n")
else:
    print("\n\nit's a tie 🫱🏻‍🫲🏼\n\n")
