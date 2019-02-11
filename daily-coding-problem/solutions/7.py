"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

mapping = [str(i) for i in range(1, 27)]


def decode(message):
    if len(message) == 1:
        return 1 if message in mapping else 0
    if len(message) == 0:
        return 0
    firstOne = message[:1]
    if firstOne in mapping:
        return 1 + decode(message[1:])
    firstTwo = message[:2]
    if firstTwo in mapping:
        return 1 + decode(message[2:])
    return 0

if __name__ == "__main__":
    assert decode('111') == 3