def ctof(cel):
    return (cel * 9/5) + 32

def ftoc(far):
    return (far - 32) * 5/9

convert = input("Type 'C2F' for Celsius to Fahrenheit, 'F2C' for Fahrenheit to Celsius:")

if convert == 'C2F':
    ctemp = float(input("Enter temperature in Celsius:"))
    result = ctof(ctemp)
    print(f"{ctemp} celsius is {result} Fahrenheit")
    
elif convert == 'F2C':
    ftemp = float(input("Enter temperature in Fahrenheit: "))
    result = ftoc(ftemp)
    print(f"{ftemp} fahrenheit is {result} Celsius")
    
else:
    print("Enter 'C2F' or 'F2C'")