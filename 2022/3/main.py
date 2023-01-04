import string

data = open("input", "r").read().split("\n")

# Split the rucksack into two parts
for i in range(data.__len__()):
    # Split the string into two halves
    data[i] = [data[i][:len(data[i])//2], data[i][len(data[i])//2:]]

# Find reacurring patterns and get priority (part 1)
charsInCommon = []

for i in data:
    charInCommon = (''.join(set(i[0]).intersection(i[1])))
    
    if charInCommon.islower():
        charAsNum = string.ascii_lowercase.index(charInCommon) + 1
    else:
        charAsNum = string.ascii_uppercase.index(charInCommon) + 27

    charsInCommon.append(charAsNum)

print(f"Part 1: {sum(charsInCommon)}")