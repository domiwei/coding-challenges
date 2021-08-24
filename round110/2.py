def run(a):
    L = len(a)-1
    ans = 0
    b = []
    for i, num in enumerate(a):
        if num%2==0:
            ans += L
            L -= 1
        else:
            b.append(num)
    
    def gcd(x, y):
        if y==0:
            return x
        return gcd(y, x%y)

    b = sorted(b, reverse=True)
    for i, num in enumerate(b):
        for j in range(i-1, -1, -1):
            if gcd(b[i], b[j])>1:
                ans += 1
    return ans


for _ in range(int(input())):
    input() 
    a = map(int, raw_input().split())
    print run(a)
