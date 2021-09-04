from collections import defaultdict

def run(cost, edges, k):
    if k==0:
        return cost[0]
    # map from node to max brach cost starting from this node

    mincostFrom1 = [float('inf')]
    branchcost = []
    inf = float('inf')
    def findmaxbranch(node, visit, branchcost): # return the cost of main branch
        visit.add(node)
        mpath = []
        for nxt in edges[node]:
            if nxt not in visit:
                mpath.append(findmaxbranch(nxt, visit, branchcost))
        #print mpath
        visit.remove(node)
        if len(mpath)==0:
            return cost[node-1]

        maxcost = max(mpath)
        # remove the max one
        mpath.remove(maxcost)
        if node == 1 and len(mpath)>0:
            mincostFrom1[0] = min(mpath)
            #print mincostFrom1

        # pairly merge mpath
        mapth = sorted(mpath)[::-1]
        for i in range(0, len(mpath), 2):
            s = sum(mpath[i:i+2])
            if i==len(mpath)-1:
                # lonely path
                branchcost.append((s, node))
            else:
                branchcost.append((s, inf))
        # return the max one
        return maxcost + cost[node-1]

    mainpath = findmaxbranch(1, set(), branchcost)
    branchcost = sorted(branchcost, key=lambda k:(-k[0], k[1]))
    topk, rest = branchcost[:k], branchcost[k:]
    #print topk, rest
    
    s = sum(s for s, _ in topk)
    exist = any(root==1 for _, root in topk)
    #print s, exist

    thecost = 0
    for c, node in rest:
        if node == 1:
            thecost = c
            break

    # case 1: top k includes the lonely path starting from 1
    if len(topk)<k or exist:
        return mainpath + s

    # case 2: top k doesn't include the lonely path from 1, so pick only top k-1
    #  1. the lonely 1 is included in rest
    #  2. the lonely 1 doesn't exist
    #print mainpath, s, mincostFrom1
    print mainpath, thecost, topk, rest, mincostFrom1
    print mainpath + s - topk[-1][0] + thecost, mainpath + s - mincostFrom1[0]

    return max(mainpath + s - topk[-1][0] + thecost, \
                mainpath + s - mincostFrom1[0])
            

def run(cost, edges, k):
    # build a simplified graph
    # st -> end, overall cost
    g = defaultdict(set)
    def build(node, visit): # return total cost, edge node
        visit.add(node)
        sedge = []
        for nxt in edges[node]:
            if nxt in visit:
                continue
            c, end = build(nxt, visit)
            sedge.append((c+cost[node], end))

        if len(edges[node])==2 and node!=0:
            # internal node
            return sedge[0]
        # articulation node
        for c, end in sedge:
            g[node].add((c-cost[node]-cost[end], end))
            g[end].add((c-cost[node]-cost[end], node))
        return cost[node], node
    build(0, set())
    #print g
    
    # bruceforce
    inf = float('inf')
    ans = [-inf]
    def find(node, jump, curcost, visit):
        if jump<0:
            return

        remove = False
        if node not in visit:
            visit.add(node)
            curcost += cost[node]
            remove = True
       
        res = -inf 
        if node==0:
            res = max(res, curcost)

        if len(g[node])>0:

            cand = [n for n in g[node]]
            for extra, nxt in cand:
                g[node].remove((extra, nxt))
                g[nxt].remove((extra, node))
                res = max(res, find(nxt, jump, curcost+extra, visit))
                g[node].add((extra, nxt))
                g[nxt].add((extra, node))
        else:
            for nxt in g:
                if len(g[nxt])>0:
                    # jump
                    res = max(res, find(nxt, jump-1, curcost, visit))
            if node!=0:
                res = max(res, find(0, jump-1, curcost, visit))

        if remove:
            visit.remove(node)
        ans[0] = max(ans[0], res)
        return
    
    find(0, k, 0, set())
    return ans[0]

for i in range(int(raw_input())):
    n, k = map(int, raw_input().split())
    cost = map(int, raw_input().split())
    edges = defaultdict(list)
    for _ in range(n-1):
        n1, n2 = map(int, raw_input().split())
        edges[n1-1].append(n2-1)
        edges[n2-1].append(n1-1)

    print 'Case #'+str(i+1)+':' + str(run(cost, edges, k))
