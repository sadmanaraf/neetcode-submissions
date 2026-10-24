
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        if len(s) == len(t):
            if s == t:
                return True
            else:
                return False
        while i < len(s):
            if j == len(t):
                return False
            elif s[i] == t[j]:
                i += 1
            j += 1
        return True


        