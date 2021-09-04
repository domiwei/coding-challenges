from collections import deque

def maxflow(g):
    n = len(g)
    target = n-1
    
    def bfs(parent):
        visit = set()
        q = deque()
        q.append(0)
        while q:
            cur = q.popleft()
            if cur == target:
                return True
            if cur in visit:
                continue
            visit.add(cur)
            for nxt, cost in enumerate(g[cur]):
                if cost == 0 or nxt in visit:
                    continue
                parent[nxt] = cur
                q.append(nxt)
        return False

    p = [-1]*n
    maxflow = 0
    while bfs(p):
        minflow = float('inf')
        cur = n-1
        while cur!=0:
            minflow = min(minflow, g[p[cur]][cur])
            cur = p[cur]

        maxflow += minflow
        # update residual net
        cur = n-1
        while cur!=0:
            g[p[cur]][cur] -= minflow
            g[cur][p[cur]] += minflow
            cur = p[cur]
        p = [-1]*n

    return maxflow

def solution(entrances, exits, path):
    n = len(path)+len(entrances)+len(exits)
    s = [0]*n
    t = [0]*n
    inf = float('inf')
    # find out cost of virtual source [start, ..., end]
    for i in entrances:
        s[i+1] = inf

    newpath = []
    for i, row in enumerate(path):
        newrow = [0]+row+[0]
        if i in exits:
            # if i is exit, connect it to virtual target
            newrow[-1] = inf
        newpath.append(newrow)

    return maxflow([s]+newpath+[t])

print solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) 
