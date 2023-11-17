def selection(arr):
    a = len(arr)
    for i in range(a):
        mini = i
        for j in range(i+1, a):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

scan = input("enter array ").split()
scan = [int(x) for x in scan]
selection(scan)
print(f"sort array is{scan}")