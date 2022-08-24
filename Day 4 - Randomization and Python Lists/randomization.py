import random

rng = random.random()
rng = rng * 5
print(rng)

#heads or tails
coin = random.randint(0,1)

if coin == 0:
    print("heads")
else:
    print("tails")