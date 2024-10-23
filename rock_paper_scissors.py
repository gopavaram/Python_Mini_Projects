import random
user_wins=0
computer_wins=0
options=['rock', 'paper', 'scissors']

while True:
    user_input=input("Enter Rock, Paper or Scissors. Enter Q if you wan to quit: ").lower()

    if user_input =='q':
        break
    
    #Important to remember ***
    if user_input not in options:
        print("Not a valid option")
        continue

    random_number=random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_pick=options[random_number]

    print("Computer picked", computer_pick+".")
    if computer_pick==user_input:
        print(f"Its a Draw. Play again")
        continue
    elif user_input=='rock' and computer_pick=='scissors':
        print("You Won")
        user_wins+=1
        continue
    elif user_input=='paper'and computer_pick=='rock':
        print("You won")
        user_wins+=1
        continue
    elif user_input=='scissors' and computer_pick=='paper':
        print("You Won")
        user_wins+=1
        continue
    else:
        print("You Lost")
        computer_wins+=1
        continue

print(f"Sore Board \nComputer Score: {computer_wins} \nUser Score: {user_wins}")
print("Bye")


