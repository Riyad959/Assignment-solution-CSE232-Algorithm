def bi_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

scan_arr = input("enter array ").split()
scan_arr = [int(x) for x in scan_arr]
num = int(input("enter the number to find "))

result = bi_search(scan_arr, num)

if result != -1:
    print(f"number {num} is found at {result}")
else:
    print("number is not found")