def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
scan = int(input("enter positive integer "))
result = sum(scan)
print(f"sum of first {scan} natural numbers is that {result}")