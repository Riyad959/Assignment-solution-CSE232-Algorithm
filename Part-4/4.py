def search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return 0

scan = input("enter array ").split()
scan = [int(x) for x in scan]
find_num = int(input("Enter the element to find: "))
result = search(scan, find_num)

if result != 0:
    print(f"The element {find_num} is found at index {result}.")
else:
    print("not found")