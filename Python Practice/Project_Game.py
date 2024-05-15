import random

# Function to roll a six-sided dice
def roll_dice():
    return random.randint(1, 6)

# Function to check if any player has won
def check_winner(scores):
    for player, score in scores.items():
        if score >= 10:  # Adjust the winning score as needed (e.g., 50 as in the previous example)
            return player
    return None

def main():
    num_players = 4
    input_list = {f"Player {i}": 0 for i in range(1, num_players + 1)}

    while True:
        for player in input_list:
            input(f"{player}, press Enter to roll the dice...")
            dice_result = roll_dice()
            print(f"{player} rolled a {dice_result}")
            input_list[player] += dice_result

            winner = check_winner(input_list)
            if winner:
                print(f"{winner} has won the game!")
                return

        # Ask the player to play again or exit the game
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing. Goodbye!")
            return

if __name__ == "__main__":
    print("WELCOME TO LUDO GAME: ")
    main()

import numpy as np

r = np.array([1, 2])
# Alternatively, you can use: r = np.array([1, 2], copy=False)

# If you want to ensure that the original array 'r' is not modified, create a copy
r_copy = np.copy(r)

# Modify the first element of the NumPy array
r_copy[0] = 999

print("Original 'r' array:", r)
print("Modified 'r_copy' array:", r_copy)
