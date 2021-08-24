from collections import defaultdict

def run(intervals, c):
    # start += 1, end remains end
    res = []
    for s, e in intervals:
        res.append([s+1, 1])
        res.append([e, -1])
    res = sorted(res)
    res.append([res[-1][0]+1, -1]) # dummy
    
    cur = 0
    prevNum = None
    s = res[0][0]
    # map from number overlap -> count
    table = defaultdict(int)
    for num, symbol in res:
        if prevNum and num != prevNum:
            # settle
            table[cur] += num-s
            s = num
        cur += symbol
        prevNum = num
    
    count = len(intervals)
    overlaps = sorted(table.keys(), reverse=True)
    for o in overlaps:
        cut = min(table[o], c)
        count += cut*o
        c -= cut
        if c==0:
            break
    return count

t = input()
for i in range(t):
    num, c = map(int, raw_input().split())
    intervals = []
    for _ in range(num):
        intervals.append(map(int, raw_input().split()))
    print 'Case #'+str(i+1)+': '+str(run(intervals, c))
