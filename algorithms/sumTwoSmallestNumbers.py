# Create a function that returns the sum of the two lowest 
# positive numbers given an array of minimum 4 positive integers.
#  No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

def sum_two_smallest_numbers(n):
    return min(n) + sorted(n)[1]

if __name__ == '__main__':
    print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))

# Another approach
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])