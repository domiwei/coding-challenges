
#  -- 4 --    30   - 50-
#       26-2x    20-x

#     a1               a2                  a3                            a4                       a5
#          (a2-a1)-2x      a3-a2-(a2-a1-2x)     a4-a3-(a3-2a2+a1+2x))
#                                                  a4-2a3+2a2-a1-2x         a5-2a4+2a3-2a2+a1 == x - 2x

#  4        17      50
#   13-2x,    33-(13-2x) = x, -x = 20
#   2x + a + a + b + b + x ==
#    2x+a ==
#    a+b ==
#    b+c ==
#    c+x ==

def solution(pegs):
    cur = 0
    for i in range(1, len(pegs)):
        cur = pegs[i]-pegs[i-1] - cur

    res = []
    if len(pegs)%2==1:
        res = [-cur, 1]# if cur<0 else None
    elif cur%3 == 0:
        res = [cur/3, 1]
    else:
        res = [cur, 3]

    #if not res or res[0]>=(pegs[-1]-pegs[-2])*res[1]:
    #    return [-1, -1]

    a, b = res[0]*2, res[1]
    r = float(a)/b
    if r<1:
        return [-1, -1]
    for i in range(1, len(pegs)):
        r = pegs[i]-pegs[i-1]-r
        if r<1:
            return [-1, -1]
    return [a, b]

print solution([4, 17, 50])
print solution([4, 30, 50])
print solution([1, 49, 50])  # 1-(48-2x)=x, x = 47
print solution([1, 2, 10])
print solution([1, 2])
print solution([1, 14, 19])
