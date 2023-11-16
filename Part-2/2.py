def find_nth_fibo(n):
    if n <= 0:
        return "input  positive num"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

scan = int(input("Enteer num to find the nth Fibonacci num"))
value = find_nth_fibo(scan)
print(f"The {scan}th fibonacci number is: {value}")
