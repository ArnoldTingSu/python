import random
def randInt(minimum = 0, maximum = 100):
    range = maximum - minimum
    num = random.random() * range + minimum
    return round(num)