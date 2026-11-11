
# Hands-On Activity: Recursive Array Toolkit
# Maria Hanna Mae T. Basierto, BSIT-2B

# 1. Sum the array
def recursive_sum(arr):
    # Base case
    if len(arr) == 0:
        return 0

    # Recursive case
    return arr[0] + recursive_sum(arr[1:])

# 2. Find the largest number
def find_largest(arr):
    # Base case
    if len(arr) == 1:
        return arr[0]

    # Recursive case
    largest_rest = find_largest(arr[1:])
    return max(arr[0], largest_rest)

# 3. Count a chosen number
def count_number(arr, target):
    # Base case
    if len(arr) == 0:
        return 0

    # Recursive case
    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)

# TESTING THE FUNCTIONS

# Test 1: Sum
print("Sum of empty array:", recursive_sum([]))
print("Sum of one number:", recursive_sum([5]))
print("Sum of array:", recursive_sum([2, 4, -3, 7]))

# Test 2: Largest Number
print("Largest number:", find_largest([3, 8, 2, 10, 5]))
print("Largest negative number:", find_largest([-8, -3, -10]))

# Test 3: Count Number
print("Count of 2:", count_number([2, 4, 2, 5, 2], 2))
print("Count of 7:", count_number([1, 2, 3, 4], 7))
print("Count in empty array:", count_number([], 2))