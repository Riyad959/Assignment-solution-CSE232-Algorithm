def bi_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid =(low + high)//2
    
    if arr[mid] == target:
        return mid
    elif arr[mid]> target:
        return bi_recursive(arr, target, low, mid - 1)
    else:
        return bi_recursive(arr, target, mid + 1, high)

sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"sort array here{sorted_arr}")
target_value = int(input("inter the element to search for="))
result = bi_recursive(sorted_arr, target_value, 0, len(sorted_arr) - 1)

if result!= -1:
    print(f"{target_value} found at index{result}")
else:
    print(f"{target_value} not found")