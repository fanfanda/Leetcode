# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = []
#     temp = []
#     for line in sys.stdin:
#         values = list(map(int, line.split(',')))
#         temp.append(values)
#     sign = n
#     while sign:
#         for index, value in enumerate(temp):
#             ans += value[:n]
#             temp[index] = value[n:]
#         sign = 0
#         for i in temp:
#             if len(i) != 0: sign = 1
#     ans = list(map(lambda x: str(x), ans))
#     print(','.join(ans))

import sys
def caffe(n, m, x, y, v):
    mins_per_time = min(v)
    mins_count = n//m + 1
    mins_time = mins_count * mins_per_time
    while True:
        res = 0
        for vi in v:
            res += int(mins_time/vi)
        if res >= n: break
    
    return 1
if __name__ == "__main__":
    # 读取第一行的n
    nums = int(sys.stdin.readline().strip())
    for i in range(nums):
        line = sys.stdin.readline().strip()
        n, m, x, y = list(map(int, line.split()))
        v = []
        for j in range(m):
            v.append(j)
        res = caffe(n, m, x, y, v)
        print(res)

# import sys 
# right = []
# false = []
# dicts = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM \t\n'
# # for line in sys.stdin:
# for line in sys.stdin:
#     sign = 0
#     line = line.strip('\n')
#     new_line = ''
#     for index, item in enumerate(line):
#         if index != 0 and line[index - 1] == ' ' and item == ' ':
#             continue
#         else:
#             new_line += item
#     for item in line:
#         if item not in dicts: 
#             false.append(new_line)
#             sign = 1
#             break
#     if not sign: right.append(new_line)
# new_right = []
# for i in right:
#     if i not in new_right: 
#         new_right.append(i)
# print(' '.join(new_right))
# #print(new_right)
# #print(false)
# print(' '.join(false))
# new_right_num = []
# for i in new_right:
#     new_right_num.append(10 % len(i))
# new_right_three = list(map(lambda x, y: x[y:] + x[:y], new_right, new_right_num))
# print(' '.join(new_right_three))
# new_right_three.sort()
# print(' '.join(new_right_three))

