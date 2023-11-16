def fibo(n):
    num = [0, 1]
    while num[-1] + num[-2] <= n:
        next_num = num[-1] + num[-2]
        num.append(next_num)
    return num

scan = int(input("maximum number for Fibonacci series"))
result = fibo(scan)
print(f"Fibonacci series up to {scan}is {result}")
