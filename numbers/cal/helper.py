
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def find_para(expression):

    tracker = {}

    for i in range(0, len(expression)):
        if expression[i] == "(":
            tracker.update({expression[i]: i})
        elif expression[i] == ")":
            tracker.update({expression[i]: i})

    if tracker == {}:
        return expression
    else:
        inside_para = expression[tracker["("] + 1: tracker[")"]]
        return inside_para
