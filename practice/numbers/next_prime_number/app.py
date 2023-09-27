

def next_prime_number():

    on = True
    num = 1

    while on:
        choice = input("Next Prime Number (y/n): ")

        if choice.lower() == "y":
            while True:
                if num == 1 or num == 2 or num == 3:
                    print(num)
                    num = num + 1
                    break
                elif num % 2 == 0 or num % 3 == 0:
                    num = num + 1
                else:
                    print(num)
                    num = num + 1
                    break
        else:
            on = False
            break
