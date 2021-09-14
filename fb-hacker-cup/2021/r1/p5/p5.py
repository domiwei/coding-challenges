from collections import defaultdict

def run(n, graph):
    visit = set()

    def rec(node):
        visit.add(node)
        # return # of nodes, min cap, all pair summation, res
        numNodes = 0
        minCap = float('inf')
        subtree = []
        total = 0
        for nxtnode, cap in graph[node]:
            if nxtnode in visit:
                continue
            subnodes, mincap, subsum = rec(nxtnode)
            total += subsum + min(micap, cap)*subnodes
            numNodes += subnodes
            subtree.append((mincap, subnodes, subsum))

        subtree = sorted(subtree)
        
        # all pair sum
        totalNodes = numNodes
        for i in range(len(subtree)):
            mincap, subnodes, subsum = subtree[i]
            totalNodes -= subnodes
            total += mincap*totalNodes*subnodes
        


for i in range(int(raw_input())):
    n = int(raw_input())
    graph = defaultdict(list)
    for _ in range(n-1):
        n1, n2, c = map(int, raw_input().split())
        graph[n1].append((n2, c))
        graph[n2].append((n1, c))
    print 'Case #' + str(i+1) + ':' + str(run(n, graph))

