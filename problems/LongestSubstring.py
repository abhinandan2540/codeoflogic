
"""# Code for finding out substring
def substring(string: str):
    string_array = list(string)
    for i in range(len(string_array)):
        for j in range(i, len(string_array)):
            print(''.join(string_array[i:j+1]))


substring('abcc')
"""

"""
def LongestSubstring(string: str):
    string_array = list(string)
    max_length = 0
    for i in range(len(string_array)):
        for j in range(i, len(string_array)):
            current = string_array[i:j+1]
            if len(current) == len(set(current)):
                max_length = max(max_length, len(current))
    return max_length


print(LongestSubstring('abcc'))
# Time complexity: O(n^3)
"""

# Using variable sliding window


def LongestSubstring(string):
    left = 0
    character = set()
    maximum_length = 0

    for right in range(len(string)):
        while string[right] in character:
            character.remove(string[left])
            left += 1
        character.add(string[right])
        maximum_length = max(maximum_length, right-left+1)
    return maximum_length


print(LongestSubstring("abcabcbb"))

# Time complexity: O(n)
# Space complexity: O(1)
