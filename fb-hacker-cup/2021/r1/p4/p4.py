import numpy as np
import math

def run(h, w, A, B):
    trans = False
    if h>w:
        h, w = w, h
        trans = True

    def valid(mat):
        for x in range(w):
            if not (1<=mat[0][x]<=1000):
                return False
        # check A, B
        right = 0
        left = 0
        for y in range(1, h):
            if not (1<=mat[y][-1]<=1000 and 1<=mat[y][0]<=1000):
                return False
            right += mat[y][-1]
            left += mat[y][0]
        
        if A!=right or B!=left:
            return False
        return True

    res = [[0]*w for _ in range(h)]
    for y in range(1, h):
        for x in range(1, w-1):
            res[y][x] = 1000

    # begin
    if h>1:
        toprow = math.ceil((max(A, B) - (1000)*(h-1)) / float(w))
        toprow = max(1, toprow)
        for x in range(w):
            res[0][x] = toprow
    else:
        toprow = A/w
        for x in range(w):
            res[0][x] = toprow
        res[0][0] += A%w

    A -= sum(res[0])
    B -= sum(res[0])
   
    if h>1:
        # top-left to bottom-right (A)
        right = A/(h-1)
        for y in range(1, h):
            res[y][-1] = right
        res[-1][-1] += A%(h-1)
    
        # top-right to bottom-left (B)
        left = B/(h-1)
        for y in range(1, h):
            res[y][0] = left
        res[-1][0] += B%(h-1)

    #print res
    if not valid(res):
        return 'Impossible'

    if trans:
        res = np.transpose(res)

    s = ['Possible']
    for row in res:
        s.append(' '.join(map(str, row)))
    return '\n'.join(s)
        
for i in range(int(raw_input())):
    N, M, A, B = map(int, raw_input().split())
    print 'Case #' + str(i+1) + ':' + str(run(N, M, A, B))

