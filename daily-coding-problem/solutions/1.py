"""
#1

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def addUpTo(k, numbers):
    for number in numbers:
        if k-number in numbers:
            return True
    return False


def describe(l, k):
    print("Tring with list {} and k={}".format(l, k))


if __name__ == "__main__":
    example1 = [10, 15, 3, 7]
    k1 = 17 
    describe(example1, k1)
    assert addUpTo(k1, example1)

    example2 = [1, 2, 3, 4]
    k2 = 100
    describe(example2, k2)
    assert not addUpTo(k2, example2)

