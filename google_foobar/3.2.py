from collections import deque

def solution(grid):
    h, w = len(grid), len(grid[0])
    visit = set()
    q = deque()
    q.append((0, 0, 0, 0)) # (y, x, count, step)
    while q:
        y, x, count, step = q.popleft()
        if (y, x, count) in visit:
            continue
        count += grid[y][x]==1
        if count>=2:
            continue
        if (y,x) == (h-1, w-1):
            return step+1

        visit.add((y,x,count))
        for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
            ny, nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w and (ny, nx, count) not in visit:
                q.append((ny, nx, count, step+1))
    return -1

print solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

