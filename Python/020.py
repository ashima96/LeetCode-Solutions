class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        stack = []
        while len(s) > 0:
            if s[0] in "{[(":
                stack.append(s[0])
                s = s[1:]
            elif len(stack)>0 and ((s[0] == ")" and stack[len(stack)-1] == "(") or (s[0] == "}" and stack[len(stack)-1] == "{") or (s[0] == "]" and stack[len(stack)-1] == "[")):
                s = s[1:]
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False


s = "()[]{}"
solution = Solution()
print(solution.isValid(s))