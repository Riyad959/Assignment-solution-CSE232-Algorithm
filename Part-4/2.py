def max(arr):
    if not arr:
        return 0

    max_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
    return max_num

scan = input("enter array ").split()
scan = [int(x) for x in scan]
max_num = max(scan)

if max_num != 0:
    print(f"maximum numb is: {max_num}")
else:
    print("array have no number.")