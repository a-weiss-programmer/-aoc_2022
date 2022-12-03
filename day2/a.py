# 0 for loss, 3 for draw, 6 for win

shape_to_letter = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

guide = {
    'A X': 3, # Rock     <- Rock
    'A Y': 6, # Rock     <- Paper
    'A Z': 0, # Rock     <- Scissors
    'B X': 0, # Paper    <- Rock 
    'B Y': 3, # Paper    <- Paper
    'B Z': 6, # Paper    <- Scissors
    'C X': 6, # Scissors <- Rock
    'C Y': 0, # Scissors <- Paper
    'C Z': 3  # Scissors <- Scissors
}

point_table = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

total_points = 0
with open('input.txt', 'r') as game_file:
    game_input = game_file.readlines()

    for line in game_input:
        second = line.split(" ")[-1].strip()
        total_points += shape_to_letter[second]
        total_points += guide[line.strip()]

print(total_points)
