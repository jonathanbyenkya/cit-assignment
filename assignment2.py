#1. Print First 10 natural numbers using while loop.
i = 1    
while i <= 10:
    print(i)
    i += 1

#2. Calculate the sum of all numbers from 1 to a given number.
#option 1
i = 1
for i in range(10):
    i += 1
    print(sum(range(10)))

#option 2
n = int(input("Enter the number: "))
sum = 0

for i in range(n + 1):
    sum += i
print(f"Sum of numbers up to {n} is {sum}")

#3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...
num = 2
for i in range(1, 30, 1):
    product = num * i
    print(product)

# 4. Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop - break
# given 'numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number % 5 == 0:
        if number > 500:
            break
        if number > 150:
            continue
    else:
        print(number)

#5. Write a program to count the total number of digits in a number using a while loop. given number `4673453`
num = 4673453
variance = 0
while num != 0:
    num = num // 10
    variance += 1
print("Total number of digits are:", variance)

#6. Display numbers from -10 to -1 using while loop    
num = -10
while num <= -1:
    print(num)
    num = num + 1 # num += 1
