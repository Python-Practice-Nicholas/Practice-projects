from math import pow


def binary_to_decimal(binary):
    decimal = 0
    binary_lst = list(str(binary))
    binary_lst.reverse()

    for i in range(0, len(binary_lst)):
        if binary_lst[i] == "1":
            binary_pow = pow(2, i)
            decimal = decimal + binary_pow
    return decimal
