def fun(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * fun(base, exponent - 1)

base_ans = float(input("Enter base"))
exponent_ans = int(input("Enter exponent"))

result = fun(base_ans, exponent_ans)
print(f"{base_ans} raised to the power of {exponent_ans} is: {result}")