def factorial(n):
    if n < 0:
        return "Factorial is always positive"
    elif n == 0 or n == 1:
        return 1
    else:
        value = 1
        for i in range(2, n + 1):
            value *= i
        return value

scan = int(input("Enter a non-negative integer: "))
result = factorial(scan)
print(f"{scan}factorial is {result}")
