import sys

# sys.stdin = open('oj_input.txt', 'r') 
nums = int(sys.stdin.readline().strip())

for i in range(nums):
    line = sys.stdin.readline().strip()
    n, r, c, s_r, s_c = list(map(int, line.split()))
    instuction = sys.stdin.readline().strip()

    matrix = [[0 for j in range(c)] for i in range(r)]
    s_r -= 1; s_c -= 1
    matrix[s_r][s_c] = 1
    
    for item in instuction:
        if item == 'N':
            while matrix[s_r - 1][s_c] == 1:
                s_r -= 1
            s_r -= 1
        elif item == 'S':
            while matrix[s_r + 1][s_c] == 1:
                s_r += 1
            s_r += 1
        elif item == 'W':
            while matrix[s_r][s_c - 1] == 1:
                s_c -= 1
            s_c -= 1
        else:
            while matrix[s_r][s_c + 1] == 1:
                s_c += 1
            s_c += 1
        matrix[s_r][s_c] = 1
    print('Case #{}: {} {}'.format(i + 1, s_r + 1, s_c + 1))