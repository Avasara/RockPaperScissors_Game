import random
import time

user_wins = 0
computer_wins = 0
draw = 0
age = 12
options = ["rock","paper","scissors"]


while True:
    computerChoice = random.randint(0, 2)
    user_input = input("Type Rock, Paper or Scissors. Q to quit: ")
    if (user_input == "q"):
        break

    if (user_input not in options):
        continue
    
    #rock is 0, paper is 1 and scissors is 2

    #random_no is an interger between 0 and 2. And options has elements between 0 and 2
    #by setting a variable equal to options and random number, then we get a computer guessor
    
    computer_guess = options[computerChoice]

    print("Computer picked: ", computer_guess, ".")

    if (user_input == "rock" and computer_guess) == "scissors":
        print("You won!")
        user_wins += 1
        print("You currently have ",user_wins,". Computer has ",computer_wins)
    elif (user_input == "paper" and computer_guess) == "rock":
        print("You won!")
        user_wins += 1
        print("You currently have ",user_wins,". Computer has ",computer_wins)
    elif (user_input == "scissors" and computer_guess) == "paper":
        print("You won!")
        user_wins += 1
        print("You currently have ",user_wins,". Computer has ",computer_wins)
    elif (user_input ==  computer_guess):
        print("Draw!")
        print("You currently have ",user_wins,". Computer has ",computer_wins)
    else:
        print("You Lost!")
        computer_wins += 1
        print("You currently have ",user_wins,". Computer has ",computer_wins)

        
print("You won" , user_wins, "times while computer won", computer_wins, "times")
if(user_wins > computer_wins):
    print("Welldone champion")
elif(user_wins == computer_wins):
    print("Good game for you both")
else:
    print("Better luck next time")


