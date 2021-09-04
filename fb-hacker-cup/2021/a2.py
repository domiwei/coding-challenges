from collections import defaultdict, deque

def run(s, table):
    inf = float('inf')
    # trans[i][j] means min path from i to j
    trans = {chr(i+ord('A')): {chr(j+ord('A')):inf for j in range(26)} for i in range(26)}
    #trans = [[inf]*26 for _ in range(26)]
    for i in range(26):
        letter = chr(i+ord('A'))
        q = deque()
        q.append((letter, 0))
        while q:
            c, step = q.popleft()
            if trans[letter][c] <= step:
                continue
            trans[letter][c] = step
            for nxt in table[c]:
                q.append((nxt, step+1))
  
    ans = inf 
    for i in range(26):
        letter = chr(i+ord('A'))
        allsteps = sum([trans[c][letter] for c in s])
        ans = min(ans, allsteps)
    return -1 if ans==inf else ans 

for i in range(int(raw_input())):
    s = raw_input()
    k = int(raw_input())
    table = defaultdict(list)
    for _ in range(k):
        f, t = list(raw_input())
        table[f].append(t)
    print 'Case #'+str(i+1)+':' + str(run(s, table))

