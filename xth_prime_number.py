def get_xth_prime_number(x):

    # initial prime number list
    prime_numbers = [2]
    num = 3

    while len(prime_numbers) < x:
        for prime_number in prime_numbers:
            if num % prime_number == 0:
                break
        else:
            prime_numbers.append(num)

        num += 2

    # return last prime number
    return prime_numbers[-1]


def main():
    print("Generate X'th prime number")
    x = int(input("Enter a number: "))
    print(get_xth_prime_number(x))


main()
