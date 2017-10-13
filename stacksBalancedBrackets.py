def is_closed(char1, char2):
    return char1 == "(" and char2 == ")" \
        or char1 == "{" and char2 == "}" \
        or char1 == "[" and char2 == "]"

def is_matched(expression):
    stack = []
    for char in expression:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        elif len(stack) == 0:
            return False
        elif char == ")" or char == "}" or char == "]":
            if not is_closed(stack.pop(), char):
                return False
    return len(stack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
