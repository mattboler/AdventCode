# dude just look at the website for description
import math

n = 312051

num = math.floor(math.ceil(math.sqrt(n))/2)
off = (n - (2*num - 1) ** 2)%(2*num)
steps = num + abs(off - num)

print(steps)
