def facto(a):
    if a < 0:
        return "Factorial cant be negative."
    elif a == 0 or a == 1:
        return 1
    else:
        value = 1
        for i in range(2, a + 1):
            value *= i
        return value

scan = int(input("Enter number: "))
answer = facto(scan)
print(f"{scan} factorial is: {answer}")