def basic_operations(num):
    even_odd_num = None
    if num % 2 != 0:
        even_odd_num = 'odd'
    else:
        even_odd_num = 'even'

    num_squared = num * num
    num_cubed = num_squared * num

    return even_odd_num, num_squared, num_cubed


def fibonaci_operation(num):
    fibonaci_sequence = [num, num]
    for n in range(8):
        next_number_in_sequence = fibonaci_sequence[n] + fibonaci_sequence[n+1]
        fibonaci_sequence.append(next_number_in_sequence)

    return fibonaci_sequence


def determine_if_prime_number(n):
    half_of_n = n // 2
    prime_number_condition = True
    for i in range(2, half_of_n + 1):
        if n // i == n / i:
            prime_number_condition = False
            break

    return prime_number_condition


def prime_number_checker(num, x):
    checked_num = num
    while True:
        checked_num += x
        if determine_if_prime_number(checked_num) == True:
            break

    if checked_num == 1:
        return None
    else:
        return checked_num


def return_closest_prime_numbers(num):
    lower_closest_number = prime_number_checker(num, -1)
    higher_closest_number = prime_number_checker(num, 1)

    return lower_closest_number, higher_closest_number


def return_prime_multipliers_of_num(num):
    list_of_primes = []
    for n in range(2, num // 2):
        if determine_if_prime_number(n):
            if num % n == 0:
                while num % n == 0:
                    list_of_primes.append(n)
                    num /= n

    return list_of_primes


def perform(num, command):
    if command == 'Basic':
        even_odd_num, num_squared, num_cubed = basic_operations(num)
        print(f"{num} is an {even_odd_num} number, which equals {num_squared} when squared and {num_cubed} when cubed.")
    elif command == 'Fibonaci':
        fibonaci_sequence = fibonaci_operation(num)
        print(f"A Fibonaci sequence based on the number {num} will look as follows:\n"
              f"{', '.join([str(x) for x in fibonaci_sequence])}")
    elif command == 'Closest Prime':
        lower_closest_number, higher_closest_number = return_closest_prime_numbers(num)
        print(f"The closest prime number lower than {num} is {lower_closest_number}.\n"
              f"The closest prime number higher than {num} is {higher_closest_number}.")
    elif command == 'Prime Multipliers':
        list_of_primes = return_prime_multipliers_of_num(num)
        print(f"The prime multipliers of {num} are as follows:\n"
              f"{', '.join([str(x) for x in list_of_primes])}")



print('This program will perform a specific operation on a whole number, depending on what you tell it')
print('Type in your number and then on a new line type in one of the following commands:')
print("'Basic', 'Fibonaci', 'Closest Prime', 'Prime Multipliers'")
num = input()
if int(num) > 0:
    num = int(num)
else:
    print('The number must be bigger than zero (0)! Please start again!')
command = input()

perform(num, command)