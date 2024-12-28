def balance(s):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

input_str = input().strip()

if balance(input_str):
    print("True")
else:
    print("False")
