import heapq

def run(intervals, c):
    # start += 1, end remains end
    res = []
    for s, e in intervals:
        res.append([s+1, 1])
        res.append([e, -1])
    res = sorted(res)
    res.append([res[-1][0]+1, -1]) # dummy
    # heap with (number overlap, start, end)
    hq = []
    cur = 0
    prevNum = None
    s = res[0][0]
    for num, symbol in res:
        if prevNum and num != prevNum:
            # settle
            heapq.heappush(hq, (-cur, s, num-1))
            s = num
        cur += symbol
        prevNum = num
    
    #print hq, res
    count = len(intervals)
    while c>0 and hq:
        numoverlap, start, end = heapq.heappop(hq)
        cut = min(c, end-start+1)
        count += cut*(-numoverlap)
        c -= cut
    return count

t = input()
for i in range(t):
    num, c = map(int, raw_input().split())
    intervals = []
    for _ in range(num):
        intervals.append(map(int, raw_input().split()))
    print 'Case #'+str(i+1)+': '+str(run(intervals, c))
