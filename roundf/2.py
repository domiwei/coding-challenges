from sortedcontainers import SortedList
import heapq

def run(happy, k, D):
    happys = [[] for _ in range(D+1)]
    removes = [[] for _ in range(D+1)]
    happymap = {}
    for i in range(len(happy)):
        s, e, h = happy[i]
        happys[s].append((h, i))
        removes[e+1].append(i)
        happymap[i] = h

    ans = 0
    topk = SortedList()
    topkValue = 0
    curattr = [] # max heap
    removeSet = set()
    for i in range(D+1):

        for r in removes[i]:
            removeSet.add(r)
            if (happymap[r], r) in topk:
                topk.discard((happymap[r], r))
                topkValue -= happymap[r]

        for h, index in happys[i]:
            if len(topk)<k or h>topk[0][0]:
                topk.add((h, index))
                topkValue += h
            else:
                heapq.heappush(curattr, (-h, index))

        while len(topk)<k and curattr:
            h, index = heapq.heappop(curattr)
            if index in removeSet:
                continue
            topk.add((-h, index))
            topkValue += -h

        while len(topk)>k:
            h, index = topk[0]
            topk.discard(topk[0])
            topkValue -= h
            heapq.heappush(curattr, (-h, index))

        ans = max(ans, topkValue)
    return ans

t = int(raw_input())
for i in range(t):
    d, n, k = map(int, raw_input().split())
    happy = []
    for _ in range(n):
        h, s, e = map(int, raw_input().split())
        happy.append((s-1,e-1,h))
    print 'Case #'+str(i+1)+': '+ str(run(happy, k, d))
