def fibo(n):
    f_fibo=0
    s_fibo=1
    print(f"{f_fibo} {s_fibo}",end=" ")
    for i in range(3,n+1):
        fibo1=f_fibo + s_fibo
        f_fibo=s_fibo
        s_fibo=fibo1
        print(f"{fibo1}",end=" ")
 
 
my_num=int(input("enter a num: "))
if my_num<=0:
    print("Please enter a positive integer")
else:
    print(f"Fibonacci series till {my_num}th ")
    fibo(my_num)
