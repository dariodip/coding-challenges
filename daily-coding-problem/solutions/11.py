"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def naive_autocomplete(strings):
    autocomplete_system = dict()

    for s in strings:
        for offset in range(1, len(s) + 1):
            prefix = s[ : offset]
            if prefix not in autocomplete_system:
                autocomplete_system[prefix] = [s]
            else:
                autocomplete_system[prefix].append(s)
    return autocomplete_system


if __name__ == "__main__":
    instance1 = ['dog', 'deer', 'deal']
    expected1 = ['deer', 'deal']
    query1 = 'de'
    
    assert naive_autocomplete(instance1)[query1] == expected1
            