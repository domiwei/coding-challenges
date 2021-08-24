from itertools import permutations

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

def run2(n):
    e = 0
    for perm in permutations(range(1, n+1)):
        cur = perm[0]
        count = 1
        for c in perm[1:]:
            if c>cur:
                count += 1
                cur = c
        e += count
    return e/float(fact(n))

def run(n):
    if n==1:
        return 1.0
    e = 0
    p = 1.0/n
    for i in range(1, n+1):
        e += i*p
        p = p/i
    return e

for i in range(int(raw_input())):
    N = int(raw_input())
    print 'Case #'+str(i+1)+': '+str(run(N))


for i in range(1, 20):
    print i, run(i), run2(i)

# 123456789

# f(n, k) -> possibilities of n cards, score=k
# f(10, 10) = 1
# f(10, 1) = 9!
# f(10, 2) = f(9,1)*9!/9! + f(8,1)*9!/8! + f(7,1)*9!/7! + f(6,1)*9!/6!
