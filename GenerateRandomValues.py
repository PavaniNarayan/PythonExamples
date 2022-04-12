import random

print(random.random())
print(random.randint(10, 30))
numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

dice =Dice()
print(dice.roll())