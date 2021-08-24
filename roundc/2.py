def run(g):
    G = 2*g
    sqrt = int(G**(0.5))
    count = 0
    for L in range(1, sqrt+1):
        if G%L!=0:
            continue
        X = G/L
        if (X&1)^(L&1)==0:
            continue
        count += 1
    return count


t = input()
for i in range(t):
    g = int(raw_input())
    #_, s = raw_input(), raw_input()
    #n, k = map(int, raw_input().split())
    #s = raw_input()
    print 'Case #'+str(i+1)+': '+str(run(g))
