import re
def tokenize(expression):
    tokens = []
    number = ""
    for i, char in enumerate(expression):
        if char.isspace():
            continue
        if char in ("(", ")", "+", "-", "*", "/"):
            if number:
                tokens.append(int(number))
                number = ""  
            if i > 0 and not (expression[i-1].isdigit() or expression[i-1] == ")"):
                if char == "+":
                    tokens.append("+")
                elif char == "-":
                    tokens.append("-")
                continue
            tokens.append(char)
        elif char.isdigit():
            number += char
    if number:
        tokens.append(int(number))
    return tokens
if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    tokens = tokenize(expression)
    print(tokens)