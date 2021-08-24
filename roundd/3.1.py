import bisect

def run(ps, ss):
    allps = []
    for p in ps:
        allps += [i for i in range(p[0], p[1]+1)]
    allps = sorted(allps)
    ans = []
    seen = set()
    for s in ss:
        index = bisect.bisect(allps, s)
        # left
        left = index-1
        while left>=0 and left in seen:
            left -= 1
        right = index
        while right<len(allps) and right in seen:
            right += 1
        if right>=len(allps) or left>=0 and abs(allps[left]-s)<=abs(allps[right]-s):
            ans.append(allps[left])
            seen.add(left)
        else:
            ans.append(allps[right])
            seen.add(right)
    return ' '.join(map(str, ans))

t = input()
for i in range(t):
    p, s = map(int, raw_input().split())
    ps = []
    for _ in range(p):
        ps.append(map(int, raw_input().split()))
    ss = map(int, raw_input().split())
    print 'Case #'+str(i+1)+': '+str(run(ps, ss))
