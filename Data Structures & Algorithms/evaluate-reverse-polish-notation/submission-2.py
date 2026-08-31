class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = None
        s = []
        for t in tokens:
            if t not in "+/*-":
                s.append(int(t))
            else:
                d1 = s.pop()
                d2 = s.pop()
                if t == "+":
                    total = d1 + d2
                    s.append(total)
                elif t == "-":
                    total = d2 - d1
                    s.append(total)
                elif t == "/":
                    total = int(d2/d1)
                    s.append(total)
                elif t == "*":
                    total = d1 * d2
                    s.append(total)
        return s[0]

        