def sum_array(arr):
    if (arr is None or len(arr) <= 2 or arr == []):
        return 0
    return sum(arr) - min(arr) - max(arr)