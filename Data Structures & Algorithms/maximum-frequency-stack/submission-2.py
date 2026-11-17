from collections import deque
class FreqStack:

    def __init__(self):
        self.stack = deque()
        return
    def push(self, val: int) -> None:
        self.stack.append(val)
        return

    def pop(self) -> int:
        def removal_inx(d,l):
            m = max(d.values())
            l1 = [k for k,v in d.items() if v == m]
            if len(l1) == 1:
                return l1[0]
            else:
                n = -1
                while True:
                    y = l[n]
                    if y not in l1:
                        n -= 1
                    else:
                        break
                    
            return y
  
        def poping(l,x):
            temp = list(l)[::-1]
            temp.pop(temp.index(x))
            l = temp[::-1]
            return deque(l)
        c = Counter(self.stack)
        y = removal_inx(c,self.stack)
        self.stack = poping(self.stack,y)
        c.subtract([y])
        return y



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()