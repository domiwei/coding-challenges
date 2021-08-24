from sys import stdout

def run(n, k):
    if (n%k)%2 == 1:
        print -1
        stdout.flush()
        return
    
    # 12345, 34567, 34578 when k=5 and middle = 3
    # middle from n to n-middle+1
    middleStart = (n%k)/2 + 1
    middleCount = k - (n%k)/2
    #middleArray = [i for i in range(midd)]
    q = []
    last = 1
    ans = 0
    if n%k != 0:
        first = [i for i in range(1, k+1)]
        sec = [i for i in range(middleStart, middleStart+k)]
        third = [i for i in range(middleStart, middleStart+middleCount)] + \
            [i for i in range(k + (n%k)/2+1, k + (n%k)+1)]
        q.append(first)
        q.append(sec)
        q.append(third)
        last = k + (n%k) + 1
    #print q, last
    while last <= n:
        q.append([i for i in range(last, last+k)])
        if q[-1][-1] > n:
            q.pop()
        last += k
   
    print q 
    for i in range(len(q)):
        #print 'wait'
        print ' '.join(['?'] + map(str, q[i]))
        stdout.flush()
        res = int(raw_input())
        ans ^= res
    print '! '+ str(ans)
    stdout.flush()

n, k = map(int, raw_input().split())
run(n, k)
