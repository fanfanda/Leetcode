def solution_count(n, m):
    if n <= 0: return 0 
    
    temp_dict = {}
    temp_dict[1] = m
    temp_dict[2] = m * (m - 1)

    for i in range(3, n + 1):
        temp_dict[i] = m * pow((m - 1), n) - temp_dict[i - 1]

    return temp_dict[n]

print(solution_count(3, 4))