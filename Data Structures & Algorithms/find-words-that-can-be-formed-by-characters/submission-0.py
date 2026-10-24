from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        char_c = Counter(chars)
        for w in words:
            word_c = Counter(w)    
            if not(word_c - char_c):
                count += len(w)
        return count