def addition(a,b):
    return a+b
c=200
def reverse(n):
    rev=0
    while(n!=0):
        rev=rev*10+n%10
        n = n//10
    return rev