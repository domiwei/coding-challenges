from collections import deque 

def run(h, w, mat):
    q = deque()
    for y in range(h):
        for x in range(w):
            if mat[y][x] != '.':
                q.append((mat[y][x], y, x))
                mat[y][x] = '.'

    def valid(y, x):
        return 0<=y<h and 0<=x<w

    if len(q) == 0:
        q.append(('R',0,0))

    # bfs
    while q:
        color, y, x = q.popleft()
        if mat[y][x] != '.':
            if mat[y][x] != color:
                return None
            continue
        mat[y][x] = color
        nextColor = 'W' if color == 'R' else 'R'
        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            ny, nx = y+dy, x+dx
            if valid(ny, nx):
                q.append((nextColor, ny, nx))
    return mat


for _ in range(int(raw_input())):
    h, w = map(int, raw_input().split())
    mat = []
    for _ in range(h):
        mat.append(list(raw_input()))
    res = run(h, w, mat)
    if not res:
        print 'NO'
    else:
        print 'YES'
        for row in res:
            print ''.join(row)
