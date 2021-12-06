import random

how_many_quick_pick = int(input(" How many quick picks? "))
for i in range(how_many_quick_pick):
    quick_picks = []
    for a in range(6):
        random_number = (random.randint(1, 45))
        while random_number in quick_picks:
            random_number = random.randint(1, 45)
        quick_picks.append(random_number)
    quick_picks.sort()
    print("".join("{:4.0f}".format(random_number) for random_number in quick_picks))
