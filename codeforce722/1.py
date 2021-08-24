def run(arr):
    arr = sorted(arr)
    l, r = 0, len(arr)-1
    ans = 0
    while l<r:
        if arr[l]<arr[r]:
            r-=1
            ans += 1
        elif arr[l]>arr[r]:
            l+=1
        else:
            break
    return ans 

t = input()
for _ in range(t):
    _, arr = raw_input(), raw_input()
    arr = map(int, arr.split())
    print run(arr)
