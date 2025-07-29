import random
def r_p_s_game():
    game_choice = ["rock","paper","scissors"]
    user_score = 0
    computer_score = 0
    print("Rules of the game: ")
    print("Enter (Rock/Paper/Scissors) to play.")
    print("Enter 'quit' to exit the game.\n")
    while True:
        
        user_choice = input("Enter your choice: ").lower()
       
        if user_choice == "quit":
            print("Thanks for playing.")
            break
            
        if user_choice not in game_choice:
            print("Invalid choice!\n")
            continue
        computer_choice = random.choice(game_choice)
        print("Computer choice: ",computer_choice)
        
        if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
            print("You won\n")
            user_score += 1
        elif computer_choice == user_choice:
            print("Tie\n")
            user_score += 1
            computer_score += 1
        else:
            print("You lose\n")
            computer_score += 1
            
        round = input("Want to play another round(Yes/No): ").lower()
        if round != "yes":
            print(f"\nYour score: {user_score} || Computer score: {computer_score}")
            if user_score > computer_score:
                print("Final Results: You WON the match.")
            elif user_score == computer_score:
                print("Final Results: Match TIE.")
            else:
                print("Final Results: You LOST the match.")
            print("\nThanks for playing.")
            break

r_p_s_game()