import numpy as np

def rowlookup(mat, h, w):
    res = []
    for y in range(h):
        row = [0]*w
        begin = 0
        for x in range(w+1):
            if x==w or mat[y][x] == '#':
                s = begin + x-1
                for dx in range(begin, x):
                    row[dx] = s
                begin = x+1
        res.append(row)
    return res

def trans(m):
    h, w = len(m), len(m[0])
    res = []
    for x in range(w):
        row = []
        for y in range(h):
            row.append(m[y][x])
        res.append(row)
    return res

def collookup(mat, h, w):
    tmat = trans(mat)
    return trans(rowlookup(tmat, w, h))

def run(mat, h, w):
    rt = rowlookup(mat, h, w)
    ct = collookup(mat, h, w)
    
    def valid(y,x):
        return 0<=y<h and 0<=x<w and mat[y][x] == '.'

    def fill(cy, cx, c):
        stack = [(cy, cx)]
        cnt = 0
        while stack:
            y, x = stack.pop()
            if not valid(y, x):
                continue
            if (y,x) in visit:
                continue
            visit.add((y,x))
            mat[y][x] = c
            cnt += 1

            # horizental
            stack.append((y,rt[y][x]-x))
            # vertical
            stack.append((ct[y][x]-y,x))
        return cnt

    count = 0
    visit = set()
    for y in range(h):
        for x in range(w):
            if mat[y][x] not in '#.' and (y, x) not in visit:
                c = mat[y][x]
                mat[y][x] = '.'
                count += fill(y, x, c)-1

    res = [str(count)]
    for row in mat:
        res.append(''.join(row))
    return '\n'.join(res)

for i in range(int(raw_input())):
    h, w = map(int, raw_input().split())
    mat = []
    for _ in range(h):
        mat.append(list(raw_input()))
    print 'Case #'+str(i+1)+': '+str(run(mat, h ,w))
