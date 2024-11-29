def find_lar(a,b,c):
    if(a>=b and a>=c):
        return a
    elif (b>=a and b>=c):
        return b
    else:
        return c
 
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
 
largest=find_lar(a,b,c)
print(f"largest among 3 num is {largest}")
