import random

dice=True

while dice:
    print(random.randint(1,6))
    roll=input("want to roll again?(Y/N):")
    if roll=="Y":
        continue
    else:
        break