def count_dub(arr):
    frequency = {}
    duplicates = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > 1:
            duplicates[num] = frequency[num]
    return duplicates

scan = input("enter array ").split()
scan = [int(x) for x in scan]
dub_num = count_dub(scan)

if dub_num:
    print("duplicate numbers and counts is-")
    for num, count in dub_num.items():
        print(f"{num} is found {count} times")
else:
    print("no duplicate here")