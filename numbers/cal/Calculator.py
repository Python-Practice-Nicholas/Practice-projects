

class Calculator:

    # Bacis Math Operations
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def find_para(self, expression):

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

    def check_operator(expression):
        number_lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        num1 = ""
        num2 = ""
        operator = ""
        indx = 0

        for i in range(indx, len(expression)):
            if expression[i] in number_lst:
                num1 = num1 + expression[i]
            else:
                operator = expression[i]
                indx = i + 1
                break

        for i in range(indx, len(expression)):
            if expression[i] in number_lst:
                num2 = num2 + expression[i]

        if operator == "+":
            return ["add", int(num1), int(num2)]
        elif operator == "-":
            return ["subtract", int(num1), int(num2)]
        elif operator == "*":
            return ["multiply", int(num1), int(num2)]
        elif operator == "/":
            return ["divide", int(num1), int(num2)]
