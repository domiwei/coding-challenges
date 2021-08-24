def run(l, k, s):
    mod = 10**9+7
    def powermap():
        m = {}
        res = 1
        m[0] = 1
        for i in range(1, half):
            m[i] = (m[i-1]*k)%mod
        return m

    half = (len(s)+1)/2
    m = powermap()
    count = 0
    # half
    for i in range(half):
        num = min(ord(s[i])-ord('a'), k)
        count += num*(m[half-i-1])
        #print num*(k**(half-i-1))

    for i in range(half, len(s)):
        if s[i]==s[len(s)-i-1]:
            continue
        elif s[i]>s[len(s)-i-1]:
            count += 1
            break
        else:
            break
    return count%(10**9+7)

t = input()
for i in range(t):
    length, k = map(int, raw_input().split())
    string = raw_input()
    #_, s = raw_input(), raw_input()
    #n, k = map(int, raw_input().split())
    #s = raw_input()
    print 'Case #'+str(i+1)+': '+str(run(length, k, string))
