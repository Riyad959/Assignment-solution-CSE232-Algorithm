def count_dig(n):
    if n < 10:
        return 1
    else:
        return 1 + count_dig(n // 10)

scan = int(input("enter positive integer: "))
sum = count_dig(scan)
print(f"number of digits is {sum}")