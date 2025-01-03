def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a,b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            a,b = stack.pop(), stack.pop()
            stack.append(int(float(b)/a))
        else:
            stack.append(int(token))
    return stack[0]

