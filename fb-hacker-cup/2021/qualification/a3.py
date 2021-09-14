from collections import defaultdict as d

def run(mat, L):
    po = {'row': d(int), 'col': d(int)}
    px = {'row': d(int), 'col': d(int)}
    empty = {'row': d(list), 'col': d(list)}
    for y in range(L):
        for x in range(L):
            symbol = mat[y][x]
            if symbol == '.':
                empty['row'][y].append(x)
                empty['col'][x].append(y)
                continue
            p = po if symbol=='O' else px
            p['row'][y] += 1
            p['col'][x] += 1

    ans = float('inf')
    count = 0
    count1coord = set()
    for dim in ['row', 'col']:
        for i in range(L):
            if po[dim][i]>0:
                continue
            res = L-px[dim][i]
            if res<ans:
                # reset
                ans = res
                count = 0

            if res==ans:
                # count plus 1
                count += 1
                if ans==1:
                    pos = (i, empty[dim][i][0]) if dim=='row' else (empty[dim][i][0], i)
                    count1coord.add(pos)
    if count==0:
        return 'Impossible'

    count = count if ans>1 else len(count1coord)
    return ' '.join([str(ans), str(count)])

for i in range(int(raw_input())):
    L = int(raw_input())
    mat = []
    for _ in range(L):
        mat.append(raw_input())
    print 'Case #'+str(i+1)+':' + str(run(mat, L))
