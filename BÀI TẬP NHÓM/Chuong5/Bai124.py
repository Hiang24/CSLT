from Bai122 import tokenize
from Bai123 import infix_to_postfix

def evaluate_postfix(postfix_tokens):
    values = []
    for token in postfix_tokens:
        if isinstance(token, int):
            values.append(token)
        else:
            right = values.pop()
            left = values.pop()
            result = eval(f"{left}{token}{right}")
            values.append(result)
    return values[0]

if __name__ == "__main__":
    expression = input("Enter a mathematical expression in infix form: ")
    tokens = tokenize(expression)
    postfix_tokens = infix_to_postfix(tokens)
    value = evaluate_postfix(postfix_tokens)
    print("Result:", value)