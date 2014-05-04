import random

glu = [3.30, 6.1]


def rand(a, b):
    i = 0
    while i < 5:
        i += 1
        print random.uniform(a, b)

rand(glu[0], glu[1])