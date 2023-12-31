import random

random.seed('class_01')

array = [random.randrange(10000) for _ in range(10)]
l_arr = len(array)
maxv = max(array)
print(maxv, array)

result = [None] * l_arr

# radix sort
div = 1
while div <= maxv:
    counts = [0] * (10)
    # counts 배열 생성
    for v in array:
        digit = v // div % 10
        counts[digit] += 1
    #
    for i in range(len(counts) - 1):
        counts[i + 1] += counts[i]

    for i in range(l_arr - 1, -1, -1):
        v = array[i]
        digit = v // div % 10
        counts[digit] -= 1
        ri = counts[digit]
        result[ri] = v

    array = result[:]
    print(array, div)
    div *= 10

exit()

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

result = [None] * l_arr
for i in range(l_arr-1, -1, -1):
    v = array[i]
    counts[v] -= 1
    ri = counts[v]
    result[ri] = v
    # print(result)

array = result
print(array)
