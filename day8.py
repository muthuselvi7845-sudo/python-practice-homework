# check palindrome
'''def palindrome(s):
    rev=s[::-1]
    if rev==s:
        return ("palindrome")
    else:
        return ("Not palindrome")
s=input("Enter a string:")
a=palindrome(s)
print((a))'''

#check palindrome using while condition
'''def palindrome(s):
    start=0
    end=len(s)-1
    while start<end:
        if s[start]!=s[end]:
            return "Not Palindrome"
        else:
            start+=1
            end-=1
    return "palindrome"
print(palindrome("malayalam"))'''


#check palindrome using for loop
def palindrome(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            return "Not Palindrome"
    return "Palindrome"
print(palindrome("malayalam"))




         

