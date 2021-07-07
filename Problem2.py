# Time Complexity : O(n)
# Auxiliary Space : O(1)
def equilibriumPoint(arr, n):
    right_sum, left_sum = 0, 0
    for i in range(1, n):
        right_sum += arr[i]

    i, j = 0, 1
    while j < n :
        right_sum -= arr[j]
        left_sum += arr[i]

        if left_sum == right_sum :
            return i + 1
        j += 1
        i += 1
    return -1
