#!/usr/bin/python3

def binarySearch(data, target, low, high):
    """
    Returns true if target is found in data from low to high inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binarySearch(data, target, low, mid - 1)
        else:
            return binarySearch(data, target, mid + 1, high)

if __name__ == '__main__':
    print(binarySearch([1, 2, 3, 4], 4, 0, 3))

