data = open('input', 'r').read().split('\n')
# Split the data into a list of lists on spaces
data = [i.split(' ') for i in data]

# Conver letters into numbers
# 0 = Rock
# 1 = Paper
# 2 = Scissors
winConditions = [
    [2, 0],
    [0, 1],
    [1, 2]
]

for i in data:
    if i[0] == 'A':
        i[0] = 0
    elif i[0] == 'B':
        i[0] = 1
    elif i[0] == 'C':
        i[0] = 2
    
    if i[1] == 'X':
        i[1] = 0
    elif i[1] == 'Y':
        i[1] = 1
    elif i[1] == 'Z':
        i[1] = 2

# Create a list of scores for each round
scores = []

for i in data:
    # The score is 
    # 1 for rock, 2 for paper, 3 for scissors
    # plus 0 if lost, 3 if it is a draw, or 6 if won.

    scores.append(i[1] +1)

    if i[0] == i[1]:
        # If it is a draw, add 3
        scores[-1] += 3
    elif [i[0], i[1]] in winConditions:
        # If it is a win, add 6
        scores[-1] += 6
    else:
        # If it is a loss, add 0
        scores[-1] += 0
    
# Print the scores (part 1)
print(f'Part 1: {sum(scores)}')

# Part 2
# Find the needed shape

# Create a list of desired outcomes
totalScore = 0
outcomes = [] 
data = open('input', 'r').read().split('\n')
# Split the data into a list of lists on spaces
data = [i.split(' ') for i in data]

# Now we need to find the shape that will give us the desired outcome
# X = Loss, Y = Draw, Z = Win
for i in data:
    roundScore = 0
    if i[1] == 'X':
        roundScore += 0

        if i[0] == 'A':
            roundScore += 3 # Scissors
        elif i[0] == 'B':
            roundScore += 1 # Rock
        elif i[0] == 'C':
            roundScore += 2 # Paper
    elif i[1] == 'Y':
        roundScore += 3

        if i[0] == 'A':
            roundScore += 1 # Rock
        elif i[0] == 'B':
            roundScore += 2 # Paper
        elif i[0] == 'C':
            roundScore += 3 # Scissors
    elif i[1] == 'Z':
        roundScore += 6

        if i[0] == 'A':
            roundScore += 2 # Paper
        elif i[0] == 'B':
            roundScore += 3 # Scissors
        elif i[0] == 'C':
            roundScore += 1 # Rock

    outcomes.append(roundScore)

print(f'Part 2: {sum(outcomes)}')