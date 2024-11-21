import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    options = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to play. Enter 'quit' to stop playing.")

    while True:
        # Get user input
        player_choice = input("Your choice: ").lower()

        # Allow the user to quit the game
        if player_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        # Validate user input
        if player_choice not in options:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Generate computer's choice
        cpu_choice = random.choice(options)
        print(f"Computer chose: {cpu_choice}")

        # Determine the winner
        if player_choice == cpu_choice:
            print("It's a tie!")
        elif(player_choice == "rock" and cpu_choice == "scissors") or \
             (player_choice == "scissors" and cpu_choice == "paper") or \
             (player_choice == "paper" and cpu_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

# Run the game
rock_paper_scissors_game()
