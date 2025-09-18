import time

print(time.time())

seed = 123324234234

def random():
    global seed
    # seed= (seed*time.time()*12443)
    seed=(seed*94+10/2453)%10
    print(seed)

for i in range(10):
    random()