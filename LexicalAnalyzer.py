import re

keywords = {"DEC": "W1", "DCL": "W2", "END": "W3", "FIXED": "W4", "IF": "W6", "PROC": "W7","THEN": "W8" "MAIN": "W9",    }
operators = {"+": "O1", "*": "O2", "<": "O3", ">": "O4", "=": "O5", ":": "O6", "<>": "O7"}
delimiters = {" ": "R1", ",": "R2", ";": "R3", "(": "R4", ")": "R5", ".": "R6"}

def lexical_analyzer(code):
    tokens = []
    words = re.findall(r"[A-Za-z_]\w*|[0-9]+(?:\.[0-9]+)?|[=,;().]", code)

    for word in words:
        if word in keywords:
            tokens.append((keywords[word], "Служебное слово", word))
        elif word in operators:
            tokens.append((operators[word], "Операция", word))
        elif word in delimiters:
            tokens.append((delimiters[word], "Разделитель", word))
        elif re.match(r"^\d+(\.\d+)?$", word):
            tokens.append(("N", "Число", word))
        else:
            tokens.append(("I", "Идентификатор", word))

    return tokens

code = "PROC MAIN; DCL (A1, A2) DEC FIXED; A1=378; A2=.73; PROC CALC; DCL (SUM, MULT) DEC FIXED; IF A1+A2<>3.2 THEN GOTO P; SUM=(A1+A2)*A2; P: MULT=A1*A2; END; END."
tokens = lexical_analyzer(code)

for token in tokens:
    print(token)
