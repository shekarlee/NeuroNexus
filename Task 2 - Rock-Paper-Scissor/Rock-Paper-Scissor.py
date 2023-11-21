#FUNCTION FOR USER INPUT
def input1(no_rounds,user_score,computer_score,Tie):
    choices=['rock','paper','scissor']
    print("choose your choice")
    print("1.rock"
           "\n2.paper",
           "\n3.scissor")
    user_input=input("select options(1,2,3): ")
    if(user_input=='1'):
        user=choices[0]
        game(no_rounds,user_score,computer_score,user,Tie)
    elif(user_input=='2'):
        user=choices[1]
        game(no_rounds,user_score,computer_score,user,Tie)
    elif(user_input=='3'):
        user=choices[2]
        game(no_rounds,user_score,computer_score,user,Tie)
    else:
        print("-----invlid choice-----")
        print("-----Choose Correct Option-----")
        print()
        input1(no_rounds,user_score,computer_score,Tie)
#FUNCTION FOR GAME RULES
def game(no_rounds,user_score,computer_score,user,Tie):
    import random
    choices=['rock','paper','scissor']
    computer=choices[random.randint(0,2)]
    print("Your choice is: ",user)
    print("Computer choice is: ",computer)
    if(user==computer):
        print("-----TIE-----")
        Tie+=1
    elif(user=='rock' and computer!='paper'):
        print("-----YOU ARE WINNER-----")
        user_score+=1
    elif(user=='scissor' and computer!='rock'):
        print("-----YOU ARE WINNER-----")
        user_score+=1
    elif(user=='paper' and computer!='scissor'):
        print("-----YOU ARE WINNER-----")
        user_score+=1
    else:
        print("-----YOU ARE LOOSER-----")
        computer_score+=1
    print("__________________________________________")
    rounds(user_score,computer_score,no_rounds,Tie)
#FUNCTION FOR CONTINUING GAME OR NOT
def rounds(user_score,computer_score,no_rounds,Tie):
    n=input("Do you want to Play another round(y/n): ")
    if(n=='y' or n=='Y'):
        no_rounds+=1
        input1(no_rounds,user_score,computer_score,Tie)
    elif(n=='n' or n=='N'):
        print("--------------------------------")
        print("Total Rounds played: ",no_rounds)
        print("Your Score is: ",user_score)
        print("Computer's score is: ",computer_score)
        print("Number of Tie's: ",Tie)
        print("--------------------------------")
        print("***GAME ENDED***")
        exit;
    else:
        print("-----invalid----")
        print("-----Choose Correct Option-----")
        rounds(user_score,computer_score,no_rounds,Tie)
#DEFAULT VALUES FOR SCORE AND ROUNDS
no_rounds=1
user_score=0
computer_score=0
Tie=0
print("***WELCOME TO ROCK-PAPER-SCISSOR GAME***")
#CALLING INPUT FUNCTION
input1(no_rounds,user_score,computer_score,Tie)