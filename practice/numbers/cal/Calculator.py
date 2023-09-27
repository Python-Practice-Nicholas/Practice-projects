

class Calculator:
    def __init__(self):
        pass

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
            return self.check_operator(expression)
        else:
            inside_para = expression[tracker["("] + 1: tracker[")"]]

            if tracker[")"] != len(expression) - 1:
                outside_para = list(expression[tracker[")"] + 1::])
                checked_inside_para = self.check_operator(inside_para)
                inside_para_value = self.select_operation(checked_inside_para)
                outside_para.insert(0, str(inside_para_value))
                return self.check_operator(outside_para)
            else:
                return self.check_operator(inside_para)

    def check_operator(self, expression):
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

    def select_operation(self, lst):

        if lst[0] == "add":
            return self.add(lst[1], lst[2])
        elif lst[0] == "subtract":
            return self.subtract(lst[1], lst[2])
        elif lst[0] == "multiply":
            return self.multiply(lst[1], lst[2])
        elif lst[0] == "divide":
            return self.divide(lst[1], lst[2])
