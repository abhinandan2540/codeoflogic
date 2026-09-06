
# Fixed size sliding window
# old sum - element leaving + element adding

def FixedSlidingWindow(array, k):
    window_sum = sum(array[:k])
    maximum = window_sum

    for right in range(k, len(array)):
        window_sum -= array[right-k]
        window_sum += array[right]
        maximum = max(maximum, window_sum)
    return maximum


array = [2, 1, 5, 1, 3, 2]
print(FixedSlidingWindow(array, 3))
