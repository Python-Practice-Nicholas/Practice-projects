
def prime_factorization(num):

    factors = [num]

    for i in range(2, 10):
        if num % i == 0:
            temp = num / i
            factors.append(int(temp))

    return factors
