class CLI(object):
    def __init__(self):
        # current map and last key, value that we wanna get
        # first index indicates the modification of dict, and 
        # second one indicates the last k,v pair on GET operation
        # (mod dict, del key set, last get kv pair)
        self.stack = [ [{}, None] ]
        
    def begin(self):
        # a new modification
        self.stack.append([{}, None])

    def commit(self):
        # merge with previous dict
        cur = self.stack.pop()
        for k, v in cur[0].items():
            self.stack[-1][0][k] = v

        # return the last k, v that wanna get
        return cur[1]

    def set(self,k, v):
        # update to last dict
        self.stack[-1][0][k] = v

    def get(self,k):
        if len(self.stack) == 1:
            return k, self.stack[-1][0][k]

        # from top one, the newest tranx
        for d, _ in self.stack[::-1]:
            if k in d:
                self.stack[-1][1] = (k, d[k])
                break
        return None

    def rollback(self):
        self.stack.pop()


'''
    def delete(self, k):
        d, delk, _ = self.stack[-1]
        if k in d:
            del d[k]
        elif len(self.stack)>1:
            # in transaction operation
            delk.add(k)
'''
# begin:
#   set x, 60
#   set y, 50
#   set t, 123
#   begin:
#     get x ---> 60
#     set x, 70
#
#     begin:
#       set x, 10000
#       get x
#       set y, 123456
#     rollback
#
#     set z, 80 
#     set y, 90
#     get x ----> 70 
#   commit:
#
#   get y -> 90
# commit
#
# get t

cli = CLI()
cli.begin()
cli.set('x', 60)
cli.set('y', 50)
cli.set('t', 123)

cli.begin()
cli.get('x')
cli.set('x', 70)

cli.begin()
cli.set('x', 10000)
cli.get('x')
cli.rollback()

cli.set('z', 80)
cli.set('y', 90)
cli.get('x')
print cli.commit()

cli.get('y')
print cli.commit()
print cli.get('t')
