

def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):   # if element is a list, recurse
            total += recursive_sum(item)
        else:                        # if element is a number, add directly
            total += item
    return total

# Example
x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]
print(recursive_sum(x))  # Output: 59



def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print Fibonacci series up to n terms
def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

# Example: print first 10 Fibonacci numbers
n = 10
print_fibonacci_series(n)

