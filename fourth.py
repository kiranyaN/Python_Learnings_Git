def factorial(n):
    res=1
    for i in range(n,1,-1):
        res=res*i
    return res
n=int(input("enter n val:"))
print("factorial val is :",factorial(n))
    
