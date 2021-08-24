from collections import defaultdict

def run(r1, r2, r3):
    count = 0
    if r1[0]+r1[2] == 2*r1[1]:
        count += 1
    if r3[0]+r3[2] == 2*r3[1]:
        count += 1
    if r1[0]+r3[0] == 2*r2[0]:
        count += 1
    if r1[2]+r3[2] == 2*r2[2]:
        count += 1
    cand = defaultdict(int)
    if (r1[0]+r3[2])%2==0:
        cand[(r1[0]+r3[2])/2] += 1
    if (r1[2]+r3[0])%2==0:
        cand[(r1[2]+r3[0])/2] += 1
    if (r1[1]+r3[1])%2==0:
        cand[(r1[1]+r3[1])/2] += 1
    if (r2[0]+r2[2])%2==0:
        cand[(r2[0]+r2[2])/2] += 1
    return count + max([0]+cand.values())

t = input()
for i in range(t):
    r1 = map(int, raw_input().split())
    r2 = map(int, raw_input().split())
    r3 = map(int, raw_input().split())
    r2 = [r2[0], None, r2[1]]
    #grid = [r1, [r2[0], None, r2[1]], r3]
    print 'Case #'+str(i+1)+': '+str(run(r1,r2,r3))
