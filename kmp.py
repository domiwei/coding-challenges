
def findLongestOverlap(a1, a2):
    def kmp(a1, a2):
        def build(s):
            nxt = [0, 0]
            j = 0
            for i in range(1, len(s)):
                while j>0 and s[i]!=s[j]:
                    j = nxt[j]
                if s[i]==s[j]:
                    j += 1
                nxt.append(j)
            return nxt

        nxt = build(a2)
        j = 0
        for i in range(len(a1)):
            if j==len(a2):
                j = nxt[j]
            while j>0 and a1[i]!=a2[j]:
                j = nxt[j]
            if a1[i] == a2[j]:
                j += 1
        return j

    return max(kmp(a1, a2), kmp(a2, a1))


a1 = 'abcdffgggttewrwcdfgggabcdffggg'
a2 = 'dffgggttewrwcabcdffgggtte'
print a1, a2, findLongestOverlap(a1, a2)
