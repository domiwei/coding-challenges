
def run(s):
    prev = None
    count = 0
    for c in s:
        if c=='F':
            continue
        if c != prev:
            count += 1
            prev = c
    return max(count-1, 0)

for i in range(int(raw_input())):
    raw_input()
    text = raw_input()
    print 'Case #' + str(i+1) + ':' + str(run(text))

