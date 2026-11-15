class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        t = []
        l = people
        lim = limit
        n = []
        while l:
            x = l.pop()
            if x == lim:
                t.append((x,))
            elif lim - x in l:
                l.remove(lim-x)
                t.append((x,lim-x))
            elif x < lim:
                n.append(x)
        while len(n) > 1:
            x = n.pop()
            y = n.pop()
            if x + y < lim:
                t.append((x,y))
            else:
                t.append((x,))
                t.append((y,))
        if len(n) == 1:
            t.append((n[0],))
        return len(t)