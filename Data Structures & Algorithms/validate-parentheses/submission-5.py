class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else:
                if stack:
                    left = stack.pop()
                else:
                    return False
                if char == ")":
                    if left != "(":
                        return False
                elif char == "]":
                    if left != "[":
                        return False
                elif char == "}":
                    if left != "{":
                        return False
        if not stack:
            return True
        else:
            return False

        