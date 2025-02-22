class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []

        for charA in tokens:
            if charA == "+":
                vals.append(vals.pop() + vals.pop())
            elif charA == "-":
                smaller = vals.pop()
                vals.append(vals.pop() - smaller)
            elif charA == "*":
                vals.append(vals.pop() * vals.pop())
            elif charA == "/":
                dividee = vals.pop()
                vals.append(int(vals.pop() / dividee))
            else:
                vals.append(int(charA))
            
        return vals[0]