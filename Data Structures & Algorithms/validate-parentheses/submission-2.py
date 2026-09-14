class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}


        for i in range(len(s)):
            if s[i] in closeToOpen:
                #first condition makes sure stack is not empty
                if stack and stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False
            