import time

lst = list(range(1000000))

# List comprehension
start = time.time()
squares = [x*x for x in lst]
print("List comprehension:", time.time() - start)

# Map
start = time.time()
squares = list(map(lambda x: x*x, lst))
print("Map:", time.time() - start)

# Loop
start = time.time()
squares = []
for x in lst:
    squares.append(x*x)
print("Loop:", time.time() - start)
