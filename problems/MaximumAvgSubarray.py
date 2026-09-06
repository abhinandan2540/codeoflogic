

def MaximumAvgSubarray(array, k):
    window_avg = sum(array[:k])
    maximum_avg = window_avg

    for right in range(k, len(array)):
        window_avg += array[right]
        window_avg -= array[right-k]
        window_avg = window_avg/k
        maximum_avg = max(maximum_avg, window_avg)
    return maximum_avg


array = [1, 12, -5, -6, 50, 3]
print(MaximumAvgSubarray(array, 4))
