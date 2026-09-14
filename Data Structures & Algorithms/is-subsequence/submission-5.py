class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new_str = ""
        n = 0

        if s == "":
            return True

        for i in range(n, len(t)):
            if len(s) != len(new_str) and t[i] == s[n]:
                n += 1
                new_str += t[i]
            
        if new_str == s:
            return True
        
        return False