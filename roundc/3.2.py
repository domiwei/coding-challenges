
def run(W, E):
    # 0->paper, 1->rock, 2->scissor
    tostr = {0:'P', 1:'R', 2:'S'}
    win = {0:2, 1:0, 2:1}
    lose = {0:1, 1:2, 2:0}
    #count = [0,0,0]
    res = ''

    # dp[state, i] = max(dp[state', i+1]) for state' transfering from state by p,r,s
    dp = {}
    def topdown(p, r, index):
        if index == 60:
            return 0, ''
        s = index-p-r
        if (p, r, index) in dp:
            return dp[p, r, index]

        res, seq = 0, ''
        count = [p,r,s]
        #print count
        for me in range(3):
            e = (W+E)/3.0
            if index>0:
                e = (count[lose[me]]*W + count[me]*E)/float(index)
            count[win[me]] += 1
            nxtres, nxtseq = topdown(count[0], count[1], index+1)
            nxtres += e
            #print me, nxtres, index
            if seq=='' or nxtres>res:
                res, seq = nxtres, tostr[me]+nxtseq
            count[win[me]] -= 1

        dp[(p,r,index)] = (res, seq)
        return res, seq
    
    resexp, seq = topdown(0,0,0)
    #print dp
    #print resexp, seq
    #accuExp += resexp
    return resexp, seq
        

accuExp = 0
t = input()
exp = input()
for i in range(t):
    w, e = map(int, raw_input().split())
    #if accuExp >= exp:
    #    print 'Case #'+str(i+1)+': '+str('P'*60)
    #    continue
    resexp, seq = run(w, e)
    #print resexp
    accuExp += resexp
    print 'Case #'+str(i+1)+': '+str(seq)
