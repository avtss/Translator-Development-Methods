def generate_code(rpn):
    stack = []
    output = []
    r_num = 1  # номер регистра

    for token in rpn.split():
        if token.isalnum():  # число или переменная
            stack.append(token)
        elif token in {'+', '-', '*', '/'}:  # операция
            b = stack.pop()
            a = stack.pop()
            reg = f"R{r_num}"
            output.append(f"{reg} = {a} {token} {b}")
            stack.append(reg)
            r_num += 1
        elif token == ":=":
            var = stack.pop()
            value = stack.pop()
            output.append(f"{var} = {value}")
        elif token == ">":
            b = stack.pop()
            a = stack.pop()
            output.append(f"IF {a} > {b} THEN")

    return "\n".join(output)


rpn_expr = "A1 3 5 2 * + := A1 10 > IF A2 A1 7 - := "
print(generate_code(rpn_expr))
