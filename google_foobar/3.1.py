def solution3(n):
    for c in n:
        if not c.isdigit():
            return 0
    n2 = list(map(int, n.lstrip('0')))
    n = list(map(int, n))
    if n!=n2:
        return 0
    
    def divideby2(k):
        cur = 0
        res = []
        for i in range(len(k)):
            cur = cur*10+k[i]
            if len(res)!=0 or cur//2!=0:
                res.append(cur//2)
            cur = cur%2
        return res
    
    def plus1(k):
        c = 1
        for i in range(len(k)-1, -1, -1):
            c = k[i]+c
            k[i] = c%10
            c = c//10
            if c == 0:
                break
        if c==1:
            k = [c]+k
        return k
    
    def minus1(k):
        k[-1] -= 1
        return k
    
    count = 0
    while len(n)>1 or n[0]>1:
        if n[-1]&1==0:
            n = divideby2(n)
        else:
            k = n[-2]*10+n[-1] if len(n)>=2 else n[-1]
            if ((k+1)/2)%2==0:
                n = plus1(n)
            else:
                n = minus1(n)
        count += 1
    return count

def solution(n):
    #print n
    def minus1(k):
        last = k[-1]
        return k[:-1]+str(int(last)-1)
    def plus1(k):
        last = k[-1]
        return k[:-1]+str(int(last)+1)
    def divide2(k):
        rest = 0
        res = []
        for i in range(len(k)):
            cur = rest*10 + int(k[i])
            res.append(str(cur//2))
            rest = cur%2
        return ''.join(res).lstrip('0')

    # Your code here
    # if n%2==1, check k=(n-1)/2
    #     if k is even, op = -1, /2
    #     if k is odd, op = +1, /2
    # else: n /= 2
    if n == '1':
        return 0
    if int(n[-1])%2==1:
        k = int(n[-2:])&2
        if k==0:
            return 2 + solution(divide2(minus1(n)))
        else:
            return 2 + solution(divide2(plus1(n)))
    return 1 + solution(divide2(n))

def solution2(n):
    n = long(n)
    count = 0
    while n>1:
        if n&1==0:
            n = n>>1
        elif n==3 or n&3 == 1:
            n -= 1
        elif n&3 == 3:
            n += 1
            
        count += 1
    return count 

print solution2('15')
#print solution('15')
print solution2('152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127152139127')
