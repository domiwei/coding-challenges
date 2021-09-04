from collections import defaultdict

def run(s):
    consonant = defaultdict(int)
    vowel = defaultdict(int)
    for c in s:
        if c in 'AEIOU':
            vowel[c] += 1
        else:
            consonant[c] += 1

    p1 = sum(vowel.values()) + 2*(sum(consonant.values())-max([0]+consonant.values()))
    p2 = sum(consonant.values()) + 2*(sum(vowel.values())-max([0]+vowel.values()))
    return min(p1, p2)

for i in range(int(raw_input())):
    s = raw_input()
    print 'Case #'+str(i+1)+':' + str(run(s))
