def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
a=input("Enter The First Number: ")
b=input("Enter The Second Number: ")
print("GCD of ",a," , ",b," is ",gcd(a,b))
