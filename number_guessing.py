import random # This is called a module. When we import random we are importing the module
r=random.randrange(10,100) #this statment will generate a random number from 10 to 100 excluding 100
r1=random.randint(0,10) #if we use randint then the 10 is also included

#project starts from here

#get input from user
get_random_number=input("Enter a number")

if get_random_number.isdigit():
    get_random_number = int(get_random_number)

    if get_random_number <= 0:
        print("Please enter a number grater than Zero")
    else:
        quit
else:
    print("Please type a number")
    quit

random_number=random.randint(0,get_random_number)

count=0

while True:
    count+=1
    guess_number=input("Guess a number")
    if guess_number.isdigit():
        guess_number=int(guess_number)
    else:
        print("Please enter a number")
        continue

    if guess_number==random_number:
        print("You got it correct")
        print("You got it correct in", count,"guesses")
        break
    elif guess_number> random_number:
        print(f"The number guessed {guess_number} is grater than random number generated")
        continue
    elif guess_number<random_number:
        print(f"The number guessed {guess_number} is less than the random number generated")
        continue



