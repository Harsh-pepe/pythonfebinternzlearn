import random as ran #ran is an alias for random

# print(ran.uniform(1.65,10.98))
#randint
#uniform
# fruits=["Apple","Banana","Orange","Grapes"]
# print(ran.choice(fruits))
deck = ["A", "K", "Q", "J", "10"]
ran.shuffle(deck)  # Shuffles the list in place
print(deck)
