import random

while True:


    print("1.rock")
    print("2.paper")
    print("3.scissors")
    option = int(input("Enter your option:"))

    if (option == 1):
        user_option = "rock"
    elif(option == 2):
       user_option = "paper"
    else:
        user_option = "scissors"

    print("user option",user_option)

    option = ["rock","paper","scissors"]
    computer_option = random.choice(option)

    print("computer option",computer_option)

    if(user_option == computer_option):
        print("Tie")
    elif(user_option == "rock"):
        if(computer_option == "paper"):
            print("computer wins")
        elif(computer_option == "scissors"):
            print("user wins")
    elif (user_option == "paper"):
        if(computer_option == "scissors"):
            print("computer wins")
        elif(computer_option == "rock"):
            print("user wins")
    elif(user_option == "scissors"):
        if(computer_option == "rock"):
            print("computer wins")
        elif(computer_option == "paper"):
            print("user wins")

    print("\n")
    print("1. next round")
    print("2.quit")
    option = int(input("enter your option:"))

    if(option == 2):
        print("Thank you for playing")
        break
    
            
    
        
