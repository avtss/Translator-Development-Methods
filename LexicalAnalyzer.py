import re

keywords = {"PROC": "W7", "MAIN": "W9", "DCL": "W2", "DEC": "W1", "FIXED": "W4", "END": "W3"}
operators = {"=": "O5"}
delimiters = {",": "R2", ";": "R3", "(": "R4", ")": "R5", ".": "R6"}

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

code = "PROC MAIN; DCL (A1, A2) DEC FIXED; A1=378; A2=.73; END."
tokens = lexical_analyzer(code)

for token in tokens:
    print(token)
