"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def productInsteadOfElement(l):
    l2 = [None for _ in range(len(l))] # init the resulting array
    for i in range(len(l)):
        if i == 0:
            l2[0] = product(l[1:])
        else:
            l2[i] = product(l[0:i]) * product(l[i+1:])
    return l2


def product(sequence):
    if sequence == []:
        return 1
    if len(sequence) == 1:
        return sequence[0]
    return sequence[0] * product(sequence[1:])


if __name__ == "__main__":
    input1 = [1, 2, 3, 4, 5]
    expected1 = [120, 60, 40, 30, 24]

    input2 = [3, 2, 1]
    expected2 = [2, 3, 6]

    assert productInsteadOfElement(input1) == expected1
    assert productInsteadOfElement(input2) == expected2
