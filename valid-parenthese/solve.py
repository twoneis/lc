class Solution:
    def isValid(self, s: str) -> bool:
        o = []
        for c in s:
            match c:
                case '(':
                    o.append(')')
                case '{':
                    o.append('}')
                case '[':
                    o.append(']')
                case ')' | '}' | ']':
                    if len(o) == 0 or o.pop() != c:
                        return False
        return (len(o) == 0)
