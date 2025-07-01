def fact(n):
    if(n<2):
        return 1
    else:
        return n*fact(n-1)


a=int(input("Enter a number: "))
b=fact(a)
print("Factorial of ",a," is: ",b)