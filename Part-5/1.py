def fibo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        result = n
    else:
        result = fibo(n - 1, memo) + fibo(n - 2, memo)
        
    memo[n] = result
    return result

scan = int(input("enter value to find Fibonacci number"))

if scan < 0:
    print("input postitive num")
else:
    result = fibo(scan)
    print(f"{scan}th fibonacci number is {result}")