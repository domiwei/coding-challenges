from collections import defaultdict

def run(cost, edges):
    def findmaxpath(node, visit):
        visit.add(node)
        mpath = 0
        for nxt in edges[node]:
            if nxt not in visit:
                mpath = max(mpath, findmaxpath(nxt, visit))
        visit.remove(node)
        return cost[node-1]+mpath

    maxpath = [0] # prevent from case: only one node in this graph
    for child in edges[1]:
        maxpath.append(findmaxpath(child, set({1})))

    p1 = max(maxpath)
    if len(maxpath)==1:
        return cost[0]+p1

    # otherwise, pick up the largest two elements 
    maxpath.remove(p1)
    return p1 + max(maxpath)+cost[0]

for i in range(int(raw_input())):
    n = int(raw_input())
    cost = map(int, raw_input().split())
    edges = defaultdict(list)
    for _ in range(n-1):
        n1, n2 = map(int, raw_input().split())
        edges[n1].append(n2)
        edges[n2].append(n1)

    print 'Case #'+str(i+1)+':' + str(run(cost, edges))
