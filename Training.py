
#This code tells the user to input name
name = input("Please enter your name: ")
print("Hello, " + name)
#line 7 assigns birth year, line 8 assigns age, line 9 compiles the result then prints it

birth_year= input("Please enter your birth year: ")
age = 2022 - int(birth_year)
print("Thank you " + name + ", you are: " + str(age) + " years old!")

first= float(input("First: "))
second= float(input("Second: "))
sum= str((first) + (second))
print("Sum: " + sum)

course = 'Python for beginners'

print(course.find('P'))
print(course.replace('for', '4'))
print("Python" in course)

#comparison operators
x= 3==1


#logical end operator
price = 5
print(not price > 30)
and
or
not

temperature = 20
if temperature > 25:
    print("its quite cold")
elif temperature < 15:  # (15, 25]
    print("its too cold")
else:
    print("i dunno brah")

weight = float(input("Weight: "))
unit = (input("(K)g or (L)bs: "))
if unit.upper == "K":
    converted = weight / 0.4539
    print("weight in lbs: " + str(converted))
else:
    converted = weight * 0.4539
    print("weight in kg: " + str(converted))


i=1
while i <= 10:
    i = i + 1
    print(i * "*")


# to list
names = ["john", "Tomi", "pepe", "Albert"]
names[1]= "Tom"
print(names)
print((names[1]))
print(names[0])
print(names)
print(names[0:3])

numbers= [1,2,3,4]
numbers.append(5)
print(numbers)

numbers.insert(0,-1)
numbers.insert(1,1.5 )
print(numbers)

numbers.remove(2)
print(numbers)

print(1 in numbers)
print(20 in numbers)

print(len(numbers))

numbers.clear()
print(numbers)

numbers= [1,2,3,4,5]
for item in numbers:
    print(item)

i = 0
while i< len(numbers):
    print(numbers[i])
    i= i + 1

numbers = range(5, 10, 2)
for items in numbers:
    print(items)

    # or
for items in range(5, 10, 2):
    print(items)
first, last=


