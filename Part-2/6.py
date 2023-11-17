def revarse_str(input_str):
    if len(input_str) <= 1:
        return input_str
    return revarse_str(input_str[1:]) + input_str[0]

scan = input("Enter string ")
result = revarse_str(scan)

print(f"reversed string is: {result}")