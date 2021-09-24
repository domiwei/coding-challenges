def run(bins):
    inf = float('inf')
    n = len(bins)
    ans = [inf]*n
    lbin = -inf
    rbin = inf
    for i in range(len(bins)):
        if bins[i]=='1':
            lbin = i
        ans[i] = min(ans[i], i-lbin)

        if bins[n-i-1]=='1':
            rbin = n-i-1
        ans[n-i-1] = min(ans[n-i-1], rbin-(n-i-1))
    
    return sum(ans) 

t = int(raw_input())
for i in range(t):
    raw_input()
    bins = list(raw_input())
    print 'Case #'+str(i+1)+': '+ str(run(bins))
