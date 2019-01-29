def isParenValid(s):
    stack, opened, closed = [], '(', ')'
    for i, c in enumerate(s):
        if c in opened:
            stack.append((c, i))
        elif c in closed:
            if not stack or stack.pop()[0] != '(':
                return False, i
    return (True, -1) if not stack else (False, stack[0][1])


assert isParenValid("(") == (False, 0)
assert isParenValid(")") == (False, 0)
assert isParenValid(")(") == (False, 0)
assert isParenValid("((") == (False, 0)
assert isParenValid("()") == (True, -1)
assert isParenValid("())") == (False, 2)
assert isParenValid("(())") == (True, -1)
