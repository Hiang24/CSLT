from Bai122 import tokenize

def infix_to_postfix(tokens):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    operators = []
    postfix = []

    for token in tokens:
        if isinstance(token, int):
            postfix.append(token)
        elif token in precedence:
            while (operators and operators[-1] != "(" and precedence[token] <= precedence.get(operators[-1], 0)):
                postfix.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                postfix.append(operators.pop())
            operators.pop()

    while operators:
        postfix.append(operators.pop())

    return postfix

if __name__ == "__main__":
    expression = input("Enter a mathematical expression in infix form: ")
    tokens = tokenize(expression)
    postfix_tokens = infix_to_postfix(tokens)
    print("Postfix expression:", postfix_tokens)