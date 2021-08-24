import heapq
from collections import defaultdict

def run2(s):
    count = defaultdict(int)
    index = defaultdict(set)
    for i, c in enumerate(s):
        index[c].add(i)
        count[c] += 1
    h = []
    for c in count:
        heapq.heappush(h, (-count[c], c))

    ans = [0]*len(s)
    while len(h)>0:
        c = heapq.heappop(h)[1]
        for i in index[c]:
            for cand in count:
                if count[cand]==0 or cand == c:
                    continue
                ans[i] = cand
                count[cand] -= 1
                break
            if ans[i] == 0:
                return 'IMPOSSIBLE'
        #print ans
    return ''.join(ans)

def run(s):
    count = defaultdict(int)
    for i, c in enumerate(s):
        count[c] += 1

    def dfs(index):
        if index==len(s):
            return ''
        
        t = s[index]
        for c in count:
            if count[c]>0 and c!=t:
                count[c] -= 1
                res = dfs(index+1)
                if res is not None:
                    return c+res
                count[c] += 1
        return None

    ans = dfs(0)
    if ans is None:
        return 'IMPOSSIBLE'
    return ans

def run(s):
    count = defaultdict(int)
    index = defaultdict(list)
    for i, c in enumerate(s):
        count[c] += 1
        index[c].append(i)
    order = []
    for c in count:
        order.append((count[c], c))
    order = sorted(order)[::-1]

    ans = [0]*len(s)
    for i in range(len(order)):
        _, c = order[i]
        for j in index[c]:
            # find out possible letter such that which is not eq to s[j]
            for k in range(len(order)):
                _, cand = order[(i+k+1)%len(order)]
                if cand != c and count[cand]>0:
                    ans[j] = cand
                    count[cand] -= 1
                    break
            if ans[j] == 0:
                return 'IMPOSSIBLE'
        #print ans, count
    return ''.join(ans)

def valid(r, s):
    for i in range(len(s)):
        if s[i] == r[i]:
            return False
    return True

def run(s):
    n = len(s)
    count = defaultdict(int)
    for i, c in enumerate(s):
        count[c] += 1
    if max(count.values()) > n//2:
        return 'IMPOSSIBLE'
    
    order = []
    for i, c in enumerate(s):
        # arrange the same letter together
        # ex: abcabcd -> aabbccd
        order.append((c, i))
    indexByOrder = sorted(order)
    
    res = [0]*n
    for i in range(n):
        c = s[indexByOrder[(i+n//2)%n][1]]
        res[indexByOrder[i][1]] = c
    r = ''.join(res)
    return r

for i in range(int(raw_input())):
    s = raw_input() 
    print 'Case #'+str(i+1)+': '+str(run(s))
