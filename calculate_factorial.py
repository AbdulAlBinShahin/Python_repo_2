def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
 
num=int(input("enter a num: "))
facto=fact(num)
print(f"fact of {num} = {facto}")
