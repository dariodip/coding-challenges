"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def missingNumber(array):
    cumSum = 0
    cumMax = -float('inf')
    cumMin = float('inf')
    array = list(set(array)) # remove duplicates
    newArray = list()
    for number in array:
        if number < 0:
            pass
        if number < cumMin:
            cumMin = number
        if number > cumMax:
            cumMax = number
        cumSum += number
        newArray.append(number)
    expectedSum = sumLowerThan(cumMax) - sumLowerThan(cumMin - 1)
    missing = expectedSum - sum(newArray)
    return missing if missing > 0 else cumMax + 1


def sumLowerThan(n):
    return n*(n+1)//2 if n % 2 == 1 else n//2*(n+1) # in order to avoid round


if __name__ == "__main__":

    example1 = [3, 4, -1, 1]
    expected1 = 2

    example2 = [1, 2, 0] 
    expected2 = 3

    assert missingNumber(example1) == expected1
    assert missingNumber(example2) == expected2