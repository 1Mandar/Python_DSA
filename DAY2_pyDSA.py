# count digits in number
number=int(input("enter any number:"))
count=0
while number>0:
    count+=1
    number//=10
print(count) 

# reverse number 12345 ==> 54321
number=int(input("enter any number:"))
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number//=10
print(reverse)


# multiplications table 1-10 11-20
num=int(input("enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
 

# fibbonacci series
n=int(input("enter number of terms:"))
a=0
b=1
print("fibbonacci series:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

# armstrong number
number=int(input("enter any number:"))
temp=number
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==number:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")


# prime number
number=int(input("enter any number:"))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:    print(number,"is not a prime number")


# pallindrome number or string
number=int(input("enter any number:"))
temp=number
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
if number==reverse:
    print(number,"is a pallindrome number")
else:    print(number,"is not a pallindrome number")
