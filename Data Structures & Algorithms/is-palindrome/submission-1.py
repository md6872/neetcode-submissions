class Solution:
    def isPalindrome(self, s: str) -> bool:
        Fpoint = 0

        #if re.search(r"^[a-zA-Z0-9]$", s):
        clean_text = ''.join(char for char in s if char.isalnum()).lower()

        Spoint = len(clean_text)-1

        if clean_text == '':
            return True
        elif clean_text[Fpoint] != clean_text[Spoint]:
            return False
        else:
            Fpoint += 1
            Spoint -= 1
            for i in range(1, len(clean_text)-1):
                if clean_text[Fpoint] != clean_text[Spoint]:
                    return False
                else:
                    Fpoint += 1
                    Spoint -= 1

        return True
                



        