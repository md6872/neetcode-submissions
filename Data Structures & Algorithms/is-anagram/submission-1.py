class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        Sdit = {}
        Tdit = {}

        for i in range(len(s)):
            Sdit[s[i]] = 1 + Sdit.get(s[i], 0)
            Tdit[t[i]] = 1 + Tdit.get(t[i], 0)
        
        return Sdit == Tdit
