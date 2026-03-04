'''angle=int(input("Enter the angle in degrees:"))
if angle<90:
    print("acute angle")
elif angle==90:
    print("right angle")
elif angle<180:
    print("obtus angle")
else:
    print("Invalid")'''

'''age1=int(input("Enter the age1:"))
age2=int(input("Enter the age2:"))
if age1>age2:
    print("First person is older")
elif age2>age1:
    print("Second person is older")
else:
    print("Both are same age")'''

'''num=int(input("Enter the number:"))
root=int(num**0.5)
if root*root==num:
    print("Perfect square")
else:
    print("Not a perfect square")'''

'''num=int(input("Enter the number:"))
if num<10 or num>50:
    print("Number lies outside range 10 to 50")
else:
    print("Number lies within the range 10 t0 50")'''
    
'''temp=float(input("Enter the tempature:"))
if temp<15:
    print("Cold")
elif temp<=30:
    print("Moderate")
elif tem>30:
    print("Hot")'''

'''ch=input("Enter a character:")
if not ch.isalnum():
    print("Special symbol")
else:
    print("Not a special symbol")'''


'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
sum=num1+num2
if sum%2==0:
    print("Even")
else:
    print("odd")'''

'''password=input("Enter the password:")
if len(password)>=8:
    print("strong")
else:
    print("weak")'''

'''num=int(input("Enter the number:"))
if num>=50 and num<=100 and num%5==0:
    print("Number is within a specific range (50 to 100) and divisible by 5")
else:
    print("Not satisified")'''

'''string1=input("Enter string1:")
string2=input("Enter string2:")
s1=len(string1)
s2=len(string2)
if s1>s2:
    Print("First string is longer")
elif s2>s1:
    print("Second string is longer")
else:
    print("Both are same len")'''
'''digit=input("Enter digit:")
if digit.isdigit:
    print("It is a digit")
else:
    print("It is not a digit")'''
'''year=int(input("Enter the year:"))
if year%100==0:
    print(" Century year")
    if year%400==0:
        print("it is a leap year")
    else:
        print("It is not a leap year")
else:
    print("Not Century year")
    if year%4==0:
        print("It is a leap year")
    else:
        print("it is not a leap year")'''
'''a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>=b and a>=c:
    print(f" {a} is greatest number")
elif b>=c and b>=a:
    print(f" {b} is greatest number")
elif c>a and c>b:
    print(f" {c} is greatest number")'''

'''a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("not a valid triangle")'''
ch=input("Enter a characters:")
first=ch[0]
if first in 'aeiou':
    print("Starts with a vowel")
else:
    print("Not starts with a vowel")




        


    

