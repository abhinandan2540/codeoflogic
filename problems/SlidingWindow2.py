
# Variable length sliding window
# window length changes according to condition

def VariableSlidingWindow(array):
    left = 0
    maximum = 0
    character = set()

    for right in range(len(array)):  # 1st line
        while array[right] in character:  # 3rd
            character.remove(array[left])  # 4th
            left += 1  # 5th
        character.add(array[right])  # 2nd line
        maximum = max(maximum, right-left+1)  # 6th
    return maximum


print(VariableSlidingWindow("abcabcbb"))
