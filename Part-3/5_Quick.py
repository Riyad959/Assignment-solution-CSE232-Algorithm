def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        
        small_value = []
        for x in arr[1:]:
            if x <= pivot:
                small_value.append(x)

        big_value = []
        for x in arr[1:]:
            if x > pivot:
                big_value.append(x)
        return quick(small_value) + [pivot] + quick(big_value)

scan = input("enter array ").split()
scan = [int(x) for x in scan]
sort_arr = quick(scan)
print(f"sorted array is {sort_arr}")