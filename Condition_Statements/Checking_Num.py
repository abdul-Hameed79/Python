# 1. WAP to check whether the user is eligible to vote or not

num = int(input("Enter a number: "))    #Take input from user

if(num % 2 == 0): print("The given number is Even")
else: print("The given number is odd")

# 2. WAP to check if a number is multible of 7 or not

num = int(input("Enter a number: "))

if(num % 7 == 0): print("The number is multiple of 7")
else: print("Entered number is not multiple of 7")

# 3. WAP to find the greatest of 3 numbers entered by user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1 > num2 and num1 > num3): 
    print(num1, "is grater")
elif(num2 > num3): 
    print(num2, "is grater")
else: print(num3, "is grater")
