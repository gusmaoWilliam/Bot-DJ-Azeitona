import random


def Dado():
    random.seed(None)
    return str(random.randrange(1, 6+1))
