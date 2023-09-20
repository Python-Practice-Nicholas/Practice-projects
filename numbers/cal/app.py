from numbers.cal.Calculator import Calculator


def cal():
    calculator = Calculator()

    while True:
        expression = input("Enter an expression or q to quit: ")

        if expression.lower() == "q":
            print("Goodbye")
            break
        lst = calculator.find_para(expression)

        print(calculator.select_operation(lst))
