name = input("Please enter your name to start: ")
print("Welcome", name, "to this adventure!")

game_over = False  # Flag to indicate if the game is over (either win or lose)

while not game_over:
    answer = input("If you want to Quit, please enter Q\nYou are on a dirt road.\nIt has come to an end, you can go left or right. Which way would you like to go?\nLeft or Right? ").lower()
    
    if answer == 'q':
        print("You have quit the game. Goodbye!")
        break  # Exit the game entirely
    
    elif answer == 'left':
        while not game_over:
            answer = input("You have come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()
            
            if answer == 'walk':
                while not game_over:
                    answer = input("You have come to a Jungle. Collect a weapon or go with bare hands? Type 'weapon' for a weapon or 'go' to go with bare hands: ").lower()
                    
                    if answer == 'weapon':
                        print("Congratulations! You won the game.")
                        game_over = True  # Set the flag to True to end the game
                        break
                    
                    elif answer == "go":
                        print("You lost. GAME OVER!")
                        game_over = True  # End the game if player loses
                        break
                    
                    else:
                        print("Invalid option. Please choose a valid option.")
                        continue
                break  # Breaks out of the river loop after completing the jungle decision
                
            elif answer == 'swim':
                print("You were killed by a crocodile. GAME OVER!")
                game_over = True  # Set flag to True to end the game
                break
            
            else:
                print("Invalid option. Please choose a valid option.")
                continue
    
    elif answer == 'right':
        print("You fell into a trap. GAME OVER!")
        game_over = True  # End the game due to trap
        break
    
    else:
        print("Invalid option. Please choose a valid option.")
