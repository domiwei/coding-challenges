def run(s):
    ans = 0
    switch = 0
    prev = None
    prevIndex = -1
    head, tail = s[0], s[0]
    curLen = 0
    mod = 10**9+7
    for i in range(len(s)):
        c = s[i]
        if c not in 'F.':
            tail = c

        if c == 'F':
            ans += switch
            curLen += 1

        if c in 'OX':
            # xx...oxf, no need to switch hand
            if prev != c:
                # xx...oxx, no need to switch hand
                # xx...offfx
                switch += prevIndex+1

            prevIndex = i
            prev = c
            ans += switch
            curLen += 1

        elif c == '.':
            if prev == head:
                ans += switch*curLen
            
            curLen *= 2

            #if 'F' in [head, tail] or prev == head:
            #    switch = (switch**2) % mod
            #else:
            #    switch = (switch*(switch+1)) % mod

            if prevIndex != -1:
                prevIndex += i

        print switch

    return ans%mod

for i in range(int(raw_input())):
    raw_input()
    text = raw_input()
    print 'Case #' + str(i+1) + ':' + str(run(text))

