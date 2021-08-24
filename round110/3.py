def run(s):
    prev = -1
    pindex = []
    for i,c in enumerate(s):
        pindex.append(prev)
        if c != '?':
            prev = i

    dp = [1]
    for i in range(1, len(s)):
        c = s[i]
        if c == '?':
            # don't care previos char
            dp.append(dp[-1]+1)
        elif pindex[i]<0:
            dp.append(i+1)
        elif (i-pindex[i])%2==1 and s[pindex[i]]==c or \
            (i-pindex[i])%2==0 and s[pindex[i]]!=c:
            # skip previous count
            # 0?1 -> count only ?1, 1
            # 1??1 -> count only ??1, ?1, 1
            dp.append(i-pindex[i])
        else:
            # 0??1 -> count all of previous possibilities
            dp.append(dp[-1]+1)
    
    #print s
    #print pindex
    #print dp
    return sum(dp)

for _ in range(int(input())):
    s = raw_input() 
    print run(s)
