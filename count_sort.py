import random

random.seed('class_01')

array = [random.randrange(15) for _ in range(30)]
l_arr = len(array)

maxv = max(array)
print(maxv, array)
# counts = [0 for _ in range(maxv + 1)]
counts = [0] * (maxv + 1)
print(counts, len(counts))

for v in array:
    counts[v] += 1
print(counts, len(counts))

# counts change to index
for i in range(len(counts) - 1):
    counts[i + 1] += counts[i]
print(counts, len(counts))

for i in range(l_arr-1, -1, -1):
    v = array[i]
    counts[v] -= 1
    ri = counts[v]
    array[ri] = v