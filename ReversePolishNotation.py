import re

PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}

def to_rpn(expression):
    output = []
    stack = []
    tokens = re.findall(r"\d+|[A-Za-z]+|[+\-*/^()]", expression)

    for token in tokens:
        if token.isalnum():  # число или переменная
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # убираем ( из стека
        else:  # операторы
            while stack and PRIORITY.get(stack[-1], 0) >= PRIORITY[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)

expr = "(a + b) * c - d / e"
print("ОПЗ:", to_rpn(expr))
