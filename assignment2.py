#1. Print First 10 natural numbers using while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

#2. Calculate the sum of all numbers from 1 to a given number.
i = 1
for i in range(10):
    i += 1
    print(sum(range(10)))

#3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...
num = 2
for i in range(1, 30, 1):
    product = num * i
    print(product)

# 4. Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next
# number
# If the number is greater than 500, then stop the loop
# given 'numbers = [12, 75, 150, 180, 145, 525, 50]:

numbers = [0, 15,30,45,60,75,90,105,120,135,150,]

for number in numbers:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number)

#5. Write a program to count the total number of digits in a number using a while loop. given number `4673453`
num = 4673453
variance = 0
while num != 0:
    num = num // 10
    variance += 1
print("Total number of digits are:", variance)

#6. Display numbers from -10 to -1 using while loop
counter = -1
while counter >= -10:
    print(counter)
    counter = counter - 1
