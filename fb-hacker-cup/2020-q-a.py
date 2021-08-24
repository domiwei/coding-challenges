def run(n, incoming, outgoing):
    ans = [[False]*n for _ in range(n)]
    for i in range(n):
        ans[i][i] = True
        if i-1>=0:
            ans[i][i-1] = outgoing[i] and incoming[i-1]
        if i+1<n:
            ans[i][i+1] = outgoing[i] and incoming[i+1]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                ans[i][j] |= ans[i][k] and ans[k][j]
    res = ['']
    for row in ans:
        res.append(''.join(['Y' if b else 'N' for b in row]))
    return '\n'.join(res)

for i in range(int(raw_input())):
    n = int(raw_input())
    incoming = [c=='Y' for c in raw_input()]
    outgoing = [c=='Y' for c in raw_input()]
    print 'Case #'+str(i+1)+':' + run(n, incoming, outgoing)
