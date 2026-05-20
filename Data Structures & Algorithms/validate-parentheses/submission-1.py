class Solution:
    def isValid(self, s: str) -> bool:
        openc = "[({"
        stack = []
        for c in s:
            if c in openc:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    match = stack.pop()
                if c == "]" and match != "[":
                    return False
                elif c == ")" and match != "(":
                    return False
                elif c == "}" and match != "{":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                

        