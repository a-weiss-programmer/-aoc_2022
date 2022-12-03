# 0 for loss, 3 for draw, 6 for win

letter_to_game_status = {
    'X': 0, # Lose
    'Y': 3, # Draw
    'Z': 6 # Win
}

guide = {
    'A X': 3, # Rock     <- Scissors
    'A Y': 1, # Rock     <- Rock
    'A Z': 2, # Rock     <- Paper
    'B X': 1, # Paper    <- Rock 
    'B Y': 2, # Paper    <- Paper
    'B Z': 3, # Paper    <- Scissors
    'C X': 2, # Scissors <- Paper
    'C Y': 3, # Scissors <- Scissors
    'C Z': 1  # Scissors <- Rock
}

total_points = 0
with open('input.txt', 'r') as game_file:
    game_input = game_file.readlines()

    for line in game_input:
        line = line.strip()
        second = line.split(" ")[-1]
        total_points += letter_to_game_status[second]
        total_points += guide[line]

print(total_points)
