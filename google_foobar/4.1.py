import itertools

def negativeCycle(graph):
    # floyd-warshall
    v = len(graph)
    path = graph

    for k in range(v):
        for i in range(v):
            for j in range(v):
                path[i][j] = min(path[i][j], path[i][k]+path[k][j])
    
    # check negative cycle
    for i in range(v):
        if path[i][i]<0:
            return True
    return False


def bf(prevnode, node, curcost, path, todo, notvisit, graph):
    if node == len(graph)-1 and curcost>=0:
        # update path if we are at bulkhead
        path, todo = path+todo, []

    if len(notvisit) == 0:
        if node == len(graph)-1:
            return path
        elif node == 0:
            # back to bulkhead
            return bf(node, len(graph)-1, curcost-graph[node][-1], path, todo, notvisit, graph)
        else:
            # back to starting point or bulkhead
            a1 = bf(node, 0, curcost-graph[node][0], path, todo, notvisit, graph)
            a2 = bf(node, len(graph)-1, curcost-graph[node][-1], path, todo, notvisit, graph)
            if len(a1)==len(a2):
                return min(a1, a2)
            else:
                return a1 if len(a1)>len(a2) else a2

    # check next points
    specialjump = [0, len(graph)-1]
    if sorted([prevnode, node]) == [0, len(graph)-1]:
        specialjump = []
    elif node == 0:
        specialjump = [len(graph)-1]
    elif node == len(graph)-1:
        specialjump = [0]

    res = []
    for jumpto in list(notvisit) + specialjump:
        addback = False
        nxtpath, nxttodo = path[:], todo[:]
        if jumpto in notvisit:
            nxtpath, nxttodo = path[:], todo+[jumpto]
            # remove it
            notvisit.remove(jumpto)
            addback = True

        cand = bf(node, jumpto, curcost-graph[node][jumpto], nxtpath, nxttodo, notvisit, graph)
        if len(cand)>len(res):
            res = cand
        elif len(cand) == len(res):
            res = min(res, cand)

        if addback:
            # add this node back into non-visit list
            notvisit.add(jumpto)

    return res

def solution(costs, timelimit):
    if negativeCycle(costs):
        return [b for b in range(len(costs)-2)]

    # bruteforce
    res = bf(None, 0, timelimit, [], [], set([i for i in range(1, len(costs)-1)]), costs)
    return sorted([b-1 for b in res])
    #return res


def test(costs, t, sol):
    clone = []
    for cost in costs:
        clone.append(cost[:])
    res = solution(clone, t)
    if res == sol:
        print True
    else:
        print res
        print sol
        print costs, t
        print clone
    print '-done-'


def convert_to_path(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path

def answer(time, time_limit):
    rows = len(time)
    bunnies = rows - 2

    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]

    for r in range(rows):
        if time[r][r] < 0:
            return [i for i in range(bunnies)]

    print time
    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list(i - 1 for i in perm))
    return None
'''
print solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
print solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
print solution(
          [[0,  1, 10, 10, 10],
          [10, 0,  1,  1,  2],
          [10, 1,  0, 10, 10],
          [10, 1,  10, 0, 10],
          [10, 10, 10, 10, 0]], 7)
print answer(
          [[0,  1, 10, 10, 10],
          [10, 0,  1,  1,  2],
          [10, 1,  0, 10, 10],
          [10, 1,  10, 0, 10],
          [10, 10, 10, 10, 0]], 7)
'''
print answer(
          [[0, 10, 10, 1, 10],
          [10, 0, 10, 10, 1],
          [10, 1, 0, 10, 10],
          [10, 10, 1, 0, 10],
          [1, 10, 10, 10, 0]], 6)


if __name__ == '__main__':
    test([[0,  1,  5,  5,  2],
          [10, 0,  2,  6,  10],
          [10, 10, 0,  1,  5],
          [10, 10, 10, 0,  1],
          [10, 10, 10, 10, 0]], 5, [0, 1, 2])


    test([[0, 1, 3, 4, 2],
          [10, 0, 2, 3, 4],
          [10, 10, 0, 1, 2],
          [10, 10, 10, 0, 1],
          [10, 10, 10, 10, 0]], 4, [])


    test([[0, 2, 2, 2, -1],
          [9, 0, 2, 2, -1],
          [9, 3, 0, 2, -1],
          [9, 3, 2, 0, -1],
          [9, 3, 2, 2, 0]], 1, [1, 2])


    test([[0,  1, 10, 10, 10],
          [10, 0,  1,  1,  2],
          [10, 1,  0, 10, 10],
          [10, 1,  10, 0, 10],
          [10, 10, 10, 10, 0]], 7, [0, 1, 2])


    test([[0, 1, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 0]], 3, [0, 1])


    test([[0, 5, 11, 11, 1],
          [10, 0, 1, 5, 1],
          [10, 1, 0, 4, 0],
          [10, 1, 5, 0, 1],
          [10, 10, 10, 10, 0]], 10, [0, 1])


    test([[0, 20, 20, 20, -1],
          [90, 0, 20, 20, 0],
          [90, 30, 0, 20, 0],
          [90, 30, 20, 0, 0],
          [-1, 30, 20, 20, 0]], 0, [0, 1, 2])


    test([[0, 10, 10, 10, 1],
          [0, 0, 10, 10, 10],
          [0, 10, 0, 10, 10],
          [0, 10, 10, 0, 10],
          [1, 1, 1, 1, 0]], 5, [0, 1])


    test([[2, 2],
          [2, 2]], 5, [])


    test([[0, 10, 10, 1, 10],
          [10, 0, 10, 10, 1],
          [10, 1, 0, 10, 10],
          [10, 10, 1, 0, 10],
          [1, 10, 10, 10, 0]], 6, [0, 1, 2])


    test([[1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1]], 1, [])

    test([[0, 0, 1, 1, 1],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]], 0, [0, 1, 2])

    test([[1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1],
          [-1, 1, 1, 1, 1]], 1, [0, 1, 2])

    test([[0, 1, 5, 5, 5, 5],
          [5, 0, 1, 5, 5, 5],
          [5, 5, 0, 5, 5, -1],
          [5, 5, 1, 0, 5, 5],
          [5, 5, 1, 5, 0, 5],
          [5, 5, 1, 1, 1, 0]]
          , 3, [0, 1, 2, 3])

    test([[0, 1, 5, 5, 5, 5, 5],
          [5, 0, 1, 5, 5, 5, 5],
          [5, 5, 0, 5, 5, 0, -1],
          [5, 5, 1, 0, 5, 5, 5],
          [5, 5, 1, 5, 0, 5, 5],
          [5, 5, 0, 5, 5, 0, 0],
          [5, 5, 1, 1, 1, 0, 0]]
          , 3, [0, 1, 2, 3, 4])

    test([[0,-1, 0, 9, 9, 9, 9, 9],  # Start
          [9, 0, 1, 9, 9, 9, 9, 9],  # 0
          [0, 9, 0, 0, 9, 9, 1, 1],  # 1
          [9, 9, 9, 0, 1, 9, 9, 9],  # 2
          [9, 9, 9, 9, 0,-1, 9, 9],  # 3
          [9, 9, 0, 9, 9, 0, 9, 9],  # 4
          [9, 9,-1, 9, 9, 9, 0, 9],  # 5
          [9, 9, 9, 9, 9, 9, 9, 0]], # bulkhead
          1, [0, 1, 2, 3, 4, 5])

    test([[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]], 0, [0, 1, 2])
    
    test([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
          0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    test([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
          5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
#print solution()
