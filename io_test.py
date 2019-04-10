import sys
from queue import PriorityQueue
sys.stdin = open('oj_input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')
res = []
for line in sys.stdin:
    line = line.strip()
    res.append(line)
print(res)
