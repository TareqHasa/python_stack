import random
def randInt(min=0   , max=100  ):
    
    num = int(random.random()*(max-min)+min)

    return num

print (randInt())
print (randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
