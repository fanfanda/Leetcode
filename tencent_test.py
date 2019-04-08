# import sys 
# import math
# inputs = sys.stdin.readline().strip().split(' ')
# n, k = list(map(lambda x: int(x), inputs))

# res = math.ceil(math.log2(n))
# if res <= k: print(res + 1)
# else: print(k + (math.pow(2, res - k - 1)) + 1)

import sys 
import math
inputs = sys.stdin.readline().strip().split(' ')
n, k = list(map(lambda x: int(x), inputs))

inputs = sys.stdin.readline().strip().split(' ')
array = list(map(lambda x: int(x), inputs))
array.sort()
sign = 1
for i in range(k):
    count = 1
    if sign:
        for index, item in enumerate(array):
            if item != 0:
                print(item)
                array = array[index:]
                array = list(map(lambda x: x - item, array))
                count = 0
                break
    if count:
        print(0)
        sign = 0