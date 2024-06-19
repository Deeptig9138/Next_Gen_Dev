import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        print("\nChoose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        user_choice = input("> ").lower()
        
        if user_choice == '4' or user_choice.startswith('q'):
            print("Thanks for playing!")
            break
        
        if user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, 3, or 4 to quit.")
            continue
        
        user_index = int(user_choice) - 1
        user_weapon = choices[user_index]
        
        computer_weapon = random.choice(choices)
        
        print(f"\nYou chose: {user_weapon}")
        print(f"Computer chose: {computer_weapon}")
        
        if user_weapon == computer_weapon:
            print("It's a tie!")
        elif (user_weapon == 'rock' and computer_weapon == 'scissors') or \
             (user_weapon == 'scissors' and computer_weapon == 'paper') or \
             (user_weapon == 'paper' and computer_weapon == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print(f"\nScoreboard - You: {user_score}, Computer: {computer_score}")

def main():
    play_game()

if __name__ == "__main__":
    main()
