import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'
def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("You lose!")
def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1
        print(f"\nScores: You - {user_score}, Computer - {computer_score}")       
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()
