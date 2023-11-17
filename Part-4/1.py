def sum(arr):
    s = 0
    for num in arr:
        s += num
    return s
                        
scan = input("enter array ").split()
scan = [int(x) for x in scan]
result = sum(scan)
print(f"The sum of the array elements is: {result}")