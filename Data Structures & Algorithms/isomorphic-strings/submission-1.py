from collections import Counter,defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_set = Counter(s)
        t_set = Counter(t)
        vocab = {}

        if len(s) != len(t):
            return False
        else:
            for s1,t1 in zip(s_set,t_set):
                vocab[s1] = t1
            valid = "".join(vocab.get(ch,"") for ch in s)
            if valid == t:
                return True
            else:
                return False

        