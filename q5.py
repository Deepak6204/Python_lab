def fac(n):
    if n==1 or n ==0:
        return 1
    
    return n*fac(n-1)

a = int(input("Enter the number you have to find the factorial of: "))
print(fac(a))