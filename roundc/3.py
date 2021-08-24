
accuExp = 0
def run(W, E):
    # 0->paper, 1->rock, 2->scissor
    tostr = {0:'P', 1:'R', 2:'S'}
    win = {0:2, 1:0, 2:1}
    lose = {0:1, 1:2, 2:0}
    count = [0,0,0]
    res = ''
    for i in range(5):
       # if i==0:
       #     res+='R'
       #     count[win[1]] += 1
            #accuExp += W/3.0
       #     continue
        
        expWE = []
        for p in range(3):
            e = count[lose[p]]*W + count[p]*E
            expWE.append(e)
        #print expWE, count
        choice = expWE.index(max(expWE))
        res += tostr[choice]
        count[win[choice]] += 1
        #accuExp += expWE[choice]/float(i) 
    return res

t = input()
exp = input()
for i in range(t):
    w, e = map(int, raw_input().split())
    print 'Case #'+str(i+1)+': '+str(run(w, e))
