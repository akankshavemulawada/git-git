num=int(input())
copy=num
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if rev==copy:
    print("its Palindrome")
else:
    print("its not palindrome")