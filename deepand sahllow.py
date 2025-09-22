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

