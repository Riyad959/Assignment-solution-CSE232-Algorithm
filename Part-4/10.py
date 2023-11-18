def peak(arr):
    if not arr:
        return None
    
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if (mid == 0 or arr[mid - 1] <= mid_value) and (mid == len(arr) - 1 or mid_value >= arr[mid + 1]):
            return mid_value
        elif mid > 0 and arr[mid - 1] > mid_value:
            high = mid - 1
        else:
            low = mid + 1

scan = input("enter array ").split()
scan = [int(x) for x in scan]
peak_element = peak(scan)

if peak_element is not None:
    print(f"peak element is {peak_element}")
else:
    print("array is empty")