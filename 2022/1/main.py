# Parse data
data = open('input', 'r').read().split('\n')
evles = [[]]
evlesSums = []

# Split the data into a list of lists
for i in data:
    if i == '':
        evles.append([])
    else:
        evles[-1].append(int(i))

# Part 1
# Find the elf with the most calories

# Add up the calories for each elf
for i in evles:
    evlesSums.append(sum(i))

# Sort the list of calories
evlesSums.sort()
print(f"Part 1: {evlesSums[-1]}")

# Part 2
# Find the total of the three most calories
totalCals = evlesSums[-1] + evlesSums[-2] + evlesSums[-3]
print(f"Part 2: {totalCals}")