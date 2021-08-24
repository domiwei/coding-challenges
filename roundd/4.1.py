class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r

def v(num, p):
    count = 0
    rest = num%p
    ismultiple = rest==0
    num -= rest
    while num and num%p==0:
        count += 1
        num/=p
    return (count, ismultiple)

def run(arr, p, qs):
    # preproccssing
    bitzero = BinaryIndexedTree(len(arr))
    bitnonzero = BinaryIndexedTree(len(arr))
    for i, num in enumerate(arr):
        value, mul = v(num, p)
        if mul:
            bitzero.update(i, value)
        else:
            bitnonzero.update(i, value)
    #print a
    # gogo
    ans = []
    for q in qs:
        if q[0] == 1:
            _, i, value = q
            arr[i-1] = value
            a[i-1] = v(value, p)
            continue
        _, S, L, R = q
        summation = 0
        for i in range(L-1, R):
            value, ismultiple = a[i]
            if ismultiple:
                summation += value*S
            else:
                summation += value
                #r = v(arr[i]**S - (arr[i]%p)**S, p)
                #summation += r
        ans.append(summation)
    return ' '.join(map(str, ans))

t = input()
for i in range(t):
    _, q, prime = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    qs = []
    for _ in range(q):
        qs.append(map(int, raw_input().split()))
    print 'Case #'+str(i+1)+': '+str(run(arr, prime, qs))
