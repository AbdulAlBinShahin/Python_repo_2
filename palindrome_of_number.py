def pali(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
 
string=input("Enter a string: ")
 
if(pali(string)):
    print("Palindrome")
else:
    print("Not Palindrome")
