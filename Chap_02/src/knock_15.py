from collections import deque

tail_deq = deque(maxlen = int(input()))
with open('../data/hightemp.txt') as f15:
    for line in f15: tail_deq.append(line.rstrip())
for line in tail_deq: print(line)

# UNIXコマンド
# tail -n 5 ../data/hightemp.txt