def howmany(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

scan = input("enter array ").split()
scan = [int(x) for x in scan]
find = int(input("enter the num  to find "))
frequency = howmany(scan, find)
print(f"frequency of {find} in the array is {frequency}")