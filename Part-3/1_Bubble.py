def bubble(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = input("enter your array")
scan = [int(x) for x in array.split()]
bubble(scan)
print(f"sort arr{scan}")