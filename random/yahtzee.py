import random
#yahtzee

total = []
num_dice = 5
# Generate and print random numbers for each dice roll
for x in range(num_dice):
    total.append(random.randint(1, 6))
print(total)
