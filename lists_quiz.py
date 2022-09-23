# 1. Write a Python program to sum all the items in a list.
#     - The list should be generated using list comprehension
#     - The size of the list should be from a user input

print("The sum of all items in a given range.")
n = int(input("Enter the range: "))
even = [x for x in range(n) if x % 2 == 0]
print(even)
print(sum(even))

# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`

words = ['abc', 'xyz', 'aba', '1221', '2', 'a', 'abdalla', '909', 'abba', '123451']

count = len([x for x in words if (len(x) >= 2 and x[-1] == x[0])])
print(count)


# 3. Write a Python program to remove duplicates from a list, given list
#     `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]

for x in fruits:
    if fruits.count(x) > 1:
        fruits.remove(x)
        print(fruits)


# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color.pop()
del color[0:5:4]
print(color)


# 5. Write a Python program to generate and print a list , where the values are square of numbers between 1 and 30 (both included) except for the first 5 elements

list = list()
for x in range(1,31):
    list.append(x*x)
    print(list[5:])
