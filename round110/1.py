
def run(a):
    g1, g2 = (a[0], a[1]), (a[2], a[3])
    if max(g1)>min(g2) and max(g2)>min(g1):
        return 'YES'
    return 'NO'

t = input()
for _ in range(int(t)):
    a = map(int, raw_input().split())
    print run(a)
