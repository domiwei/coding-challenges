from collections import deque

def solution(src, dest):
    #Your code here
    y, x = src%8, src/8
    ty, tx = dest%8, dest/8
    jump = [(1,2),(-1,2),(1,-2),(-1,-2)]
    jump += [(dx, dy) for dy, dx in jump]

    visit = set()
    q = deque()
    q.append((y, x, 0))
    while q:
        y, x, step = q.popleft()
        if (y, x) in visit:
            continue
        if (y, x) == (ty, tx):
            return step
        visit.add((y,x))
        for dy, dx in jump:
            if 0<=y+dy<8 and 0<=x+dx<8 and (y+dy, x+dx) not in visit:
                q.append((y+dy, x+dx, step+1))
    return -1

print solution(0, 1)
print solution(19, 36)
