def insertion(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

scan = input("enter array ").split()
scan = [int(x) for x in scan]
insertion(scan)
print(f"sort array in descending order is {scan}")