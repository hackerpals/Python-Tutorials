#!/usr/bin/python
import random

for i in range(1,29):
    numbers = random.sample(range(1,41), 6)
    powerball = random.sample(range(1,21), 1)
    print(i ," . ", numbers , " Powerball ", powerball )
