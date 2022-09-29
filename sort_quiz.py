#1. Your task is to create slightly different animals, which should have the same properties and methods, but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, as the animals have different sounds.

class Animal():
    def __init__(self, name: str, age: int, food: list):
        self.name = name
        self.age = age
        self.food = food
    
    def get_name(self):
        return f"The animal is a {self.name}."

    def set_name(self, name):
        self.name = name
        return f"The goat has a name {self.name}"

    def get_age(self):
        return f"This animal is {self.age} years old."

    def set_age(self, new_age):
        self.age = new_age
        return f"The above animal has an age of {new_age}."

    def get_food(self):
        return f"The animal {self.name} feeds on {self.food}"

    def add_food(self, food):
        food = self.food.append(food)
        return f"The new diet is {self.food}."

    def remove_food(self, food):
        food = self.food.remove(food)
        return f"The new diet is {self.food}"

class Cat(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Meow"

class Dog(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Woff"

class Fish(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Blub"

class Cow(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Muu"

animal = Animal("Goat", "8", ["Grass", "plantain", "Starch"])
print(animal.get_name())
print(animal.set_name('Eobard'))
print(animal.get_age())
print(animal.set_age(8))
print(animal.get_food())
print(animal.add_food('leaves'))
print(animal.remove_food('Starch'))

cat = Cat("Snow", 6, ['meat', 'milk'], "Meow")
dog = Dog("Scooby", 10, ['meat', 'milk'], "Woof")
fish = Fish("Fluufy", 2, ['weed'], "Blub")
cow = Cow("Ron", 4, ['grass', 'feed mix'], "Muu")


#2. When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)
print(cat)
print(dog)
print(fish)
print(cow)


#2.  The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6
def days_taken(depth):
    days = 0
    if depth < 7:
        days += 1
        return days
    else:
        new_depth = depth - 7 + 2
        return days_taken(new_depth)

print(days_taken(50))


#3. Write a function that takes a list of numbers and returns the largest number in the list.
def largest_number(arr):
    return max(arr)

num = largest_number([23, 25, 46, 63, 96, 74])
print(num)


#4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
def letters_count(sentence):
    lower_case_count = 0
    upper_case_count = 0
    for i in sentence:
        if i in ascii.lowercase_letters:
            lower_case_count += 1
        if i in ascii.upper_letters:
            upper_case_count += 1
            
    return f"The upper case count is {upper_case_count} and the lower case count is {lower_case_count}"


#5. Using Object Oriented Programming, write a program that implements a dice game. The game should have two players, and each player should have a name and a score. The game should have a method called play that takes two players as arguments and simulates the game. The game should be played as follows:
#.  Each player rolls a die.
# The player with the highest roll wins the round.
# The winner gets one point added to their score.
# The game ends when one player has 5 points.
# The player with the most points at the end of the game wins.
# The program should print out the winner's name and score.
# If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.
# Write a Python program that lists out all the default as well as custom properties of the class.
def dice_game():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def play(self, player1, player2):
        while player1.score < 5 and player2.score < 5:
            player1_roll = player1.roll()
            player2_roll = player2.roll()
            if player1_roll > player2_roll:
                player1.score += 1
                print(f'{player1.name} wins!')
            elif player2_roll > player1_roll:
                player2.score += 1
                print(f'{player2.name} wins!')
            else:
                print('Its a tie')

        if player1.score > player2.score:
            print(f"{player1.name} is the winner")
        else:
            print(f"{player2.name} is the winner")

    def roll(self):
        import random
        roll = random.randint(1,6)
        print(f'{self.name} rolled a {roll} choice')
        return roll


#6. Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.

class Stack:
    def __init__(self):
        self.stack = list()

    # check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        # push element on the stack
        self.stack.append(data)

    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

    def pop(self):
        # pop element from the stack
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.show())
    print(s.pop())
    print(s.show())
    print(s.peek())
    print(s.size())
    s.push('Hello')
    s.push('data')
    print(s.show())
    print(s.peek())
    print(s.pop())
    print(s.show())




        
#7. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.

print([x for x in range(10) if x**2])



#8. Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).
list_1 = list()
maximum = 5

def isEmpty():
    return len(list_1) == 0    


def isFull():
    return len(list_1) == maximum

def enqueue(element):
    if not isFull():
        list_1.insert(0,element)
        return list_1
    else:
        return 'list is already full'


def dequeue():
    if not isEmpty():
        list_1.pop()
        return list_1

    else:
        return 'yo the list is already empty'

def display(f):
    print(f)

display(enqueue(6))
display(enqueue(7))
display(enqueue(8))
display(enqueue(9))
display(enqueue(10))
display(isFull())
display(enqueue(1))
display(dequeue())
display(dequeue())
display(dequeue())
display(dequeue())
display(dequeue())
display(isEmpty())
display(dequeue())

#Using a while loop, implement merge sort algorithm.
def mergeSort(array):
    if len(array) > 1:

        midPoint = len(array)//2
        leftArray = array[:midPoint]
        rightArray = array[midPoint:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        x = 0
        y = 0
        z = 0

        while x < len(leftArray) and y < len(rightArray):
            if leftArray[x] < rightArray[y]:
                array[z] = leftArray[x]
                x += 1
            else:
                array[z] = rightArray[y]
                y += 1
            z += 1

        
        while x < len(leftArray):
            array[z] = leftArray[x]
            x += 1
            z += 1

        while y < len(rightArray):
            array[z] = rightArray[y]
            y += 1
            z += 1


def printSortedArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    mergeSort(numbers)
