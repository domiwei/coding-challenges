def solution2(L):
    # ds:
    #   key: num, value: [num of elements divides key]
    #             value: [count of this elem, total count]
    # 1,1,1,1,1
    # 1: 0
    # 1: 1 -> s += 0 [0]
    # 1: 2 -> s += 0 [0, 1]
    # 1: 3 -> s += 0+1 [0, 1, 2]
    # 1: 4 -> s += 0+1+2 [0, 1, 2, 3]
    # 1,2,3,4,5,6
    # 0,1,1,2,1,3
    # 0,0,0,1,1,3
    table = {}
    ans = 0
    for num in sorted(L):
        if num not in table:
            table[num] = [0, 0]
        divideCount = 0
        for k in table.keys():
            if num%k!=0:
                continue
            ans += table[k][1]
            divideCount += table[k][0]
        #print table
        table[num][0] += 1
        table[num][1] += divideCount
        #print ans
    #print table
    return ans

def solution(L):
    ans = 0
    L = sorted(L)
    count = []
    for i in range(len(L)):
        total = 0
        for j in range(i):
            if L[i]%L[j]!=0:
                continue
            ans += count[j]
            total += 1
        count.append(total)
        #print L[i], ans
    #print count
    return ans

print solution([1,1,1])==1
print solution([1,1,1,1])==4
print solution([6,5,4,3,2,1])==3
# [0, 1, 1, 2, 1, 3, 1, 3]
print solution([1,2,3,4,5,6,7,8])==6 # 124,126,128,136,148,248
print solution([1,1,1,1,1,1])==20
print solution([1,2])==0
print solution([1,1,2])==1
print solution([1,1,2,2])==4
print solution([1,1,2,2,2])==10
print solution([1,1,2,2,2,3])==11
print solution([4,8,4,16])==2 # 4,4,8, 4,4,16,  4
print solution([1,2,4,8,16])==10
