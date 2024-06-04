def linear_search(arr, x):
    """
    Searches for the given element in the list using Linear Search algorithm.

    Parameters:
    arr (list): The list to be searched.
    x: The element to be searched.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    """
    Searches for the given element in the sorted list using Binary Search algorithm.

    Parameters:
    arr (list): The sorted list to be searched.
    x: The element to be searched.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def interpolation_search(arr, x):
    """
    Searches for the given element in the sorted list using Interpolation Search algorithm.

    Parameters:
    arr (list): The sorted list to be searched.
    x: The element to be searched.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def exponential_search(arr, x):
    """
    Searches for the given element in the sorted list using Exponential Search algorithm.

    Parameters:
    arr (list): The sorted list to be searched.
    x: The element to be searched.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    if arr[0] == x:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= x:
        i = i * 2
    return binary_search(arr[:min(i, n)], x)

def jump_search(arr, x):
    """
    Searches for the given element in the sorted list using Jump Search algorithm.

    Parameters:
    arr (list): The sorted list to be searched.
    x: The element to be searched.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

# Test the searching functions
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array:", arr)
print("Linear Search (5):", linear_search(arr, 5))
print("Binary Search (6):", binary_search(arr, 6))
print("Interpolation Search (7):", interpolation_search(arr, 7))
print("Exponential Search (8):", exponential_search(arr, 8))
print("Jump Search (9):", jump_search(arr, 9))
