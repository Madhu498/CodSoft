import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        
    def get_user_choice(self):
        while True:
            choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
            if choice in self.choices:
                return choice
            print("Invalid choice! Please try again.")
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        
        winning_combinations = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        
        if winning_combinations[user_choice] == computer_choice:
            return "user"
        return "computer"
    
    def display_result(self, user_choice, computer_choice, winner):
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            self.user_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1
            
        print(f"\nScore - You: {self.user_score} Computer: {self.computer_score}")
    
    def play_again(self):
        return input("\nDo you want to play again? (yes/no): ").lower().startswith('y')
    
    def play_game(self):
        print("Welcome to Rock Paper Scissors!")
        
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, winner)
            
            if not self.play_again():
                print("\nThanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()