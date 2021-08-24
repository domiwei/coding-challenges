def run(arr):
    #print arr
    if len(arr) == 1:
        return 1

    arr = sorted(arr)
    if arr[0]>0:
        return 1

    ans = 0
    d = arr[1]-arr[0]
    start = 0
    for i in range(len(arr)):
        if arr[i]<=0:
            ans += 1
            start = i
            if i>0:
                d = min(d, arr[i]-arr[i-1])

    for i in range(start+1, len(arr)):
        #print arr[i], arr[start], d
        if arr[i]<=d:
            ans += 1
            break
    #           left
    # -4, -3, -2, 0, 1, 4, 6
    # -5, -3, 0, 2, 5
    return ans

t = input()
for _ in range(t):
    _, arr = raw_input(), raw_input()
    arr = map(int, arr.split())
    print run(arr)
