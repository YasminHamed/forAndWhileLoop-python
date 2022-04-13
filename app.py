# 1)program to print first 10 natural numbers

number = 1
while number <= 10:
    print (number)
    number+=1



# 2)program to print first 10 even numbers

for number in range(0,11,2): # range (start num, stop at, add num)
    print(number)



# 3)program to print first 10 odd numbers

for number in range(1,10,2): # range (start num, stop at, add num)
    print(number)



# 4)program to print first 10 even numbers in reverse order.

for number in range(10,1,-2): # range (start num, stop at, add num)
    print(number)



# 5)program to find the sum of the digits of a number accepted from user

n = int(input("Enter number"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of numbers is: ", sum)



# 6)Accept 10 numbers from the user and display their average. using Loop

num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))
num3 = int(input('Enter the third number'))
num4 = int(input('Enter the fourth number'))
num5 = int(input('Enter the fifth number'))
num6 = int(input('Enter the sixth number'))
num7 = int(input('Enter the seventh number'))
num8 = int(input('Enter the eighth number'))
num9 = int(input('Enter the ninth number'))
num10 = int(input('Enter the tenth number'))

# list with int(input)
num_list = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
res1 = 0
for num in num_list:
    res1 += num
avg1 = res1 / len(num_list)
print("sum is: ", res1, "Average is: ", avg1)