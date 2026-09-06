
def MinimumSizeSubarray(array, k):
    window_sum = sum(array[:k])
    minimum_sum = window_sum

    for right in range(k, len(array)):
        window_sum += array[right]
        window_sum -= array[right-k]
        minimum_sum = min(minimum_sum, window_sum)
    return minimum_sum


array = [1, 12, -5, -6, 50, 3]
print(MinimumSizeSubarray(array, 3))
