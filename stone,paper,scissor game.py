import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return 'win'
    else:
        return 'lose'

def play_game():
    print("Welcome to stone, Paper, Scissor!")
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose a power stone, Paper, or Scissor:")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ['stone', 'paper', 'scissor']:
            print("Invalid choice. Please choose 'stone,,', 'paper', or 'scissor'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            print("It's a tie!")
        elif result == 'win':
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Score: You {user_score} - Computer {computer_score}")
            break

if __name__ == "__main__":
    play_game()