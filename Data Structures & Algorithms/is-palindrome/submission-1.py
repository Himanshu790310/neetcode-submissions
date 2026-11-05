class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = ''
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    w += i.lower()
                else:
                    w += i
        while len(w) > 1:
            if w[0] == w[-1]:
                w = w[1:-1]
            else:
                return False
        return True

        