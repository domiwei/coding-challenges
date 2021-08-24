def run(mat, h, w):
    # pay attention! DO NOT use recursion in this case because it may lead to max recur limit exceeds
    # but still give us RE
    def valid(y,x):
        return 0<=y<h and 0<=x<w and mat[y][x] == '.'

    def fill(cy, cx, c):
        stack = [(cy,cx)]
        count = 0
        while stack:
            y, x = stack.pop()
            if not valid(y, x):
                continue

            mat[y][x] = c
            count += 1

            # horizental
            l, r = x, x
            while l>=0 and mat[y][l]!='#': l-=1
            while r<w and mat[y][r]!='#': r+=1
            u, d = y, y
            while u>=0 and mat[u][x]!='#': u-=1
            while d<h and mat[d][x]!='#': d+=1
            stack.append((y,l+r-x))
            stack.append((u+d-y,x))
        return count

    count = 0
    for y in range(h):
        for x in range(w):
            if mat[y][x] not in '#.':
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
