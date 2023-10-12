import random

random.seed('class_01')

array = [random.randrange(100) for _ in range(30)]
print(array)

# pairs = list(map(lambda v : (-v, v), array))
# print(pairs)
#
# import heapq
#
# # 힙 상태가 된 배열, but 반대로 되어있음 (min heap)
# # collection이 오면 첫 번째 원소를 비교
# heapq.heapify(pairs)
# heapified = list(map(lambda  p : p[1], pairs))
# # max heap
# print(heapified)

# [88, 86, 80, 66, 81, 69, 65, 60, 64, 66, 37, 64, 66, 57, 37, 51, 33, 55, 0, 30, 39, 16, 3, 46, 26, 0, 50, 11, 40, 36]

# 내가 자식보다 작으면 내려감, 더 내려갈 수 있는지 확인
def downHeap(arr, root, size):
    # 중간고사 몇부터 시작인지, 0부터 시작으로 +1
    child = root * 2 + 1
    
    # if 30 < size
    # pyramid of doom vs early return => 너무 많은 들여쓰기
    if child < size: return # if lc not exists

    right_c_idx = child + 1
    if right_c_idx < size: # if rc exists
        if arr[child] < arr[right_c_idx]:
            child = right_c_idx

    if arr[root] >= arr[child]: return

    arr[root], arr[child] = arr[child], arr[root]
    # 더 내려갈 수 있는지
    downHeap(arr. child, size)

l_arr = len(array)
# 배열의 절반부터 0까지
for i in range(l_arr // 2 - 1, 0 - 1, -1):
    downHeap(array, i, l_arr)
