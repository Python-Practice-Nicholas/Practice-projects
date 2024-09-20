from math import pow, floor


def binary_to_decimal(binary):
    decimal = 0
    binary_lst = list(str(binary))
    binary_lst.reverse()

    for i in range(0, len(binary_lst)):
        if binary_lst[i] == "1":
            binary_pow = pow(2, i)
            decimal = decimal + binary_pow
    return decimal


def decimal_to_binary(decimal):
    binary = ""
    not_zero = True
    while not_zero:
        remainder: str = str(decimal % 2)
        binary = remainder + binary
        decimal = floor(decimal / 2)

        if decimal == 0:
            not_zero = False

    return binary


def swap_back(binary):
    dec = binary_to_decimal(binary)
    bina = decimal_to_binary(dec)
    print(dec)
    print(bina)