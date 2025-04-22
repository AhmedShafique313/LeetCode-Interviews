def valid_parentheses(arr):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in arr:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return 'Invalid'
        else:
            return 'Invalid'
    return 'valid' if not stack else 'invalid'


if __name__ == "__main__":
    test_cases = [
        "()",        # Valid
        "()[]{}",    # Valid
        "(]",        # Invalid
        "([)]",      # Invalid
        "{[]}",      # Valid
        "(",         # Invalid
        "]",         # Invalid
        "abc",       # Invalid
    ]
    
    for expression in test_cases:
        print(f"{expression}: {valid_parentheses(expression)}")