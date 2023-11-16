def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

scan = int(input("Enter number: "))
if is_prime(scan):
    print(f"{scan}a prime number.")
else:
    print(f"{scan}not a prime number.")