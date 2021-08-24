
def run(a):
    a = [0]+a+[0]
    score = 0
    for i in range(1, len(a)):
        score += abs(a[i]-a[i-1])
        if i<len(a)-1 and a[i]>a[i-1] and a[i]>a[i+1]:
            score -= a[i] - max(a[i-1], a[i+1])
    return score

for _ in range(int(raw_input())):
    raw_input()
    a = map(int, raw_input().split())
    print run(a)
