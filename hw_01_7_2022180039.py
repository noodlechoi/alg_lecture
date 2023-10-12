words = [

  '2022180039', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'class01', 'idolize', 'romance', 'overestimate', 'revive', 'smell',

  'toast', 'singe', 'inlay', 'field', 'speed', 'farad', 'adult', 'pansy', 'crawl', 'smith', 'exude',

  'froze', 'litho', 'inuit', 'fakir', 'noddy', 'sheen', 'sandy', 'gaffe', 'spark', 'cavil', 'tenor',

  'clonk', 'stung', 'boult', 'inapt', 'taker', 'cliff', 'shine', 'sable', 'agile', 'evens', 'pluck',

  'blade', 'niece', 'paste', 'theft', 'young', 'bonny', 'aggro', 'bevel', 'rebel', 'clown', 'quote',

  'horsy', 'wrong', 'hindu', 'acute', 'sloop', 'tuner', 'expel', 'motel', 'divan', 'gesso', 'strop',

  'lance', 'lifer', 'dunce', 'lemur', 'scree', 'basic', 'wring', 'graph', 'conch', 'favor', 'anise',

  'value', 'queue', 'poppy', 'staid', 'snook', 'spurt', 'canto', 'sprat', 'first', 'sidle', 'douse',

]


def downHeap(arr, root, size):
    # 중간고사 몇부터 시작인지, 0부터 시작으로 +1
    child = root * 2 + 1

    # if 30 >= size
    # pyramid of doom vs early return => 너무 많은 들여쓰기
    if child >= size: return  # if lc not exists

    right_c_idx = child + 1
    if right_c_idx < size:  # if rc exists
        if arr[child] < arr[right_c_idx]:
            child = right_c_idx

    if arr[root] >= arr[child]: return

    arr[root], arr[child] = arr[child], arr[root]
    # 더 내려갈 수 있는지
    downHeap(arr, child, size)


l_arr = len(words)
# 배열의 절반부터 0까지
for i in range(l_arr // 2 - 1, 0 - 1, -1):
    downHeap(words, i, l_arr)

for size in range(l_arr - 1, 0, -1):
    words[0], words[size] = words[size], words[0]
    downHeap(words, 0, size)

print(words)