def run(s):
    ans = 0
    switch = 0
    prev = None
    prevIndex = -1
    for i in range(len(s)):
        c = s[i]
        if c != 'F':
            # xx...oxf, no need to switch hand
            if prev != c:
                # xx...oxx, no need to switch hand
                # xx...offfx
                switch += prevIndex+1

            prevIndex = i
            prev = c

        ans += switch

    return ans%(10**9+7)

for i in range(int(raw_input())):
    raw_input()
    text = raw_input()
    print 'Case #' + str(i+1) + ':' + str(run(text))

