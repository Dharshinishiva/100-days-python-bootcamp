def isValid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in pairs:  # closing bracket
            if stack and stack[-1] == pairs[ch]:
                stack.pop()  # correct match → remove from stack
            else:
                return False  # mismatch
        else:
            stack.append(ch)  # opening bracket → put in stack

    return not stack  # true if stack empty at end
