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

def collookup(mat, h, w):
    tmat = np.transpose(mat)
    return np.transpose(rowlookup(tmat, w, h))

def run(mat, h, w):
    rt = rowlookup(mat, h, w)
    ct = collookup(mat, h, w)
    
    def valid(y,x):
        return 0<=y<h and 0<=x<w and mat[y][x] == '.'

    def fill(y, x, c):
        if not valid(y, x):
            return 0
        if (y,x) in visit:
            return 0
        visit.add((y,x))
        mat[y][x] = c

        # horizental
        #l, r = 0, w-1
        #for i in range(1, w):
        #    if x-i>=0 and mat[y][x-i] == '#':
        #        l = max(l, x-i+1)
        #    if x+i<w and mat[y][x+i] == '#':
        #        r = min(r, x+i-1)
        c1 = fill(y, rt[y][x]-x, c)

        # vertical
        #u, d = 0, h-1
        #for i in range(1, h):
        #    if y-i>=0 and mat[y-i][x] == '#':
        #        u = max(u, y-i+1)
        #    if y+i<h and mat[y+i][x] == '#':
        #        d = min(d, y+i-1) 
        c2 = fill(ct[y][x]-y, x, c)
        return c1+c2+1

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
    h, w = map(int, raw_input().split(' '))
    mat = []
    for _ in range(h):
        mat.append(list(raw_input()))
    print 'Case #'+str(i+1)+': '+str(run(mat, h ,w))
