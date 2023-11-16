def sum(arr, n):
    if n == 0:
        return 0
    else:
        result = 0
        for i in range(n):
            result += arr[i]
        return result

scan = input("inter num: ")
array = []
current_number = ""

for char in scan:
    if char != ' ':
        current_number += char
    else:
        array.append(int(current_number))
        current_number = ""

if current_number != "":
    array.append(int(current_number))

size = len(array)

result = sum(array, size)
print(f"The sum is{result}")