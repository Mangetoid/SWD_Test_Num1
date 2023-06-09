def factorial(n):
    # Check for negative case
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Check for special cases: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Initialize the result variable
    result = 1

    # Multiply numbers from 2 to n
    for i in range(2, n + 1):
        result *= i

    return result


def count_zeros(n):
    # Convert the factorial to a string
    factorial_str = str(n)

    # Initialize a counter for zeros
    zero_count = 0

    # Iterate through the string in reverse
    for digit in reversed(factorial_str):
        if digit == '0':
            zero_count += 1
        else:
            break

    return zero_count


try:
    # Prompt the user for an input integer
    num = int(input("Enter a non-negative integer: "))

    # Calculate the factorial
    factorial_result = factorial(num)

    # Count the zeros in the factorial
    zeros = count_zeros(factorial_result)

    # Print the factorial and the count of zeros
    print("Factorial of", num, ":", factorial_result)
    print("Number of zeros after the last non-zero digit:", zeros)

except ValueError as error:
    print("Error:", str(error))
