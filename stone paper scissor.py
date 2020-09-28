import random
user_wins = 0
comp_wins = 0

'''def User_Choose():
    user_choice = input("choose Rock, Paper, Scissors: ")
    if user_choice in ["rock", "Rock","r","R"]:
        user_choice = "r"
    elif user_choice in ["paper","Paper","p","P"]:
        user_choice = "p"
    elif user_choice in ["scissors","Scissors","s","S"]:
        user_choice = "s"
    else:
        print("I don't understand, please try again")
        User_Choose()
    return user_choice'''

def Comp_Choose():
    comp_choice = random.randint(1,3)
    if comp_choice ==1:
        comp_choice="r"
    elif comp_choice==2:
        comp_choice="p"
    elif comp_choice==3:
        comp_choice="s"
    return comp_choice

#user_choice = User_Choose()
comp_choice = Comp_Choose()

user_choice=input("choose Rock, Paper or Scissors:")

if user_choice in ["rock", "Rock","r","R"]:
        if comp_choice=="r":
            print("user selected Rock and computer selected Rock, match tied!!")
        elif comp_choice=="p":
            print("user selected Rock and computer selected Paper, Computer Wins!!")
            comp_wins+=1
        elif comp_choice=="s":
            print("user selected Rock and computer selected Scissors, User Wins!!")
            user_wins+=1

elif user_choice in ["paper","Paper","p","P"]:
        if comp_choice=="r":
            print("user selected Paper and computer selected Rock, User Wins!!")
            user_wins+=1
        elif comp_choice=="p":
            print("user selected Paper and computer selected Paper, match tied!!")
        elif comp_choice=="s":
            print("user selected Paper and computer selected Scissors, Computer Wins!!")
            comp_wins+=1

elif user_choice in ["scissors","Scissors","s","S"]:
        if comp_choice=="r":
            print("user selected Scissors and computer selected Rock, Computer Wins!!")
            comp_wins+=1
        elif comp_choice=="p":
            print("user selected Scissors and computer selected Paper, User Wins!!")
            user_wins+=1
        elif comp_choice=="s":
            print("user selected Scissors and computer selected Scissors, match tied!!")

print("User Wins: "+ str(user_wins))
print("Computer Wins: "+ str(comp_wins))

user_choice=input("Do you want to play again (y/n): ")
if user_choice in["yes","Yes","y","Y"]:
    print("Let's play again!!")
    Comp_Choose()
elif user_choice in ["no","No","n","N"]:
    if user_wins > comp_wins:
        print("User won the game by",user_wins,"-",comp_wins)
    else:
        print("Computer won the game by",comp_wins,"-",user_wins)
    print("Game has ended!!")


    
