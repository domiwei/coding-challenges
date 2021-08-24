class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
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
    zero = [None for _ in range(len(arr))]
    nonzero = [None for _ in range(len(arr))]
    for i, num in enumerate(arr):
        value, mul = v(num, p)
        #print value, mul
        if mul:
            bitzero.update(i+1, value)
            zero[i] = value
        else:
            bitnonzero.update(i+1, value)
            nonzero[i] = value

    # gogo
    ans = []
    for q in qs:
        if q[0] == 1:
            _, i, value = q
            if zero[i-1]!=None:
                bitzero.update(i, -zero[i-1])
                zero[i-1] = None
            else:
                bitnonzero.update(i, -nonzero[i-1])
                nonzero[i-1] = None

            newvalue, mul = v(value, p)
            if mul:
                bitzero.update(i, newvalue)
                zero[i-1] = newvalue
            else:
                bitnonzero.update(i, newvalue)
                nonzero[i-1] = newvalue
            continue
        _, S, L, R = q
        #print bitzero.sum(R)-bitzero.sum(L) + bitnonzero.sum(R)-bitnonzero.sum(L)
        ans.append((bitzero.sum(R)-bitzero.sum(L-1))*S + bitnonzero.sum(R)-bitnonzero.sum(L-1))
    return ' '.join(map(str, ans))

t = input()
for i in range(t):
    _, q, prime = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    qs = []
    for _ in range(q):
        qs.append(map(int, raw_input().split()))
    print 'Case #'+str(i+1)+': '+str(run(arr, prime, qs))
