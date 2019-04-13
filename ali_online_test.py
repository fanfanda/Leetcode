import sys
# sys.stdin = open('oj_input.txt', 'r')
m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
if k == 1: print(0)
if k == 2: print(1)
result = 1

if k > 2: print(result%10000)




import sys
# sys.stdin = open('oj_input.txt', 'r')
n = int(sys.stdin.readline().strip())
prob = []
for i in range(n):
    prob.append(float(sys.stdin.readline().strip()))
prob = prob * 100
result, count = 0.0, 0
prob_invert = list(map(lambda x: 1 - x, prob))
while count < len(prob):
    if count == 0:
        result += prob[count]
    else:
        temp = 1
        for i in range(count):
            temp = temp * prob_invert[i]
        result += temp * prob[count]
    count += 2
print('%.04f' % round(result, 4))