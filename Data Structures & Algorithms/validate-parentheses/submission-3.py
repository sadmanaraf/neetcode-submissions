class Solution:
    def isValid(self, s: str) -> bool:
        left = set('([{')
        right = set('}])')
        pairs = {'(':')','{':'}','[':']'}
        stack = []
        for i, b in enumerate(s):
            if b in left:
                stack.append(b)

            else: 
                if not stack or b != pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return not stack
        