def multiply(x,y):
    if x<10 or y<10:
        return x*y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    z0 = multiply(low1, low2)
    z2 = multiply(high1, high2)
    z1 = multiply((low1 + high1), (low2 + high2))

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the secong number "))
result = multiply(num1,num2)
print(f"The result using karatsuba algorithm is",result)