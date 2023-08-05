
print("Question 1")

message ="hello world"
print(message)

print("Question 2")
quote = "Before getting there must be giving"
quote = quote.replace("getting", "receiving")
print(quote)

#question 3
commands = ["enable","config t", "interface g0/0", "ip address 192.168.1.1 255.255.255.0","no shutdown", "exit"]
i =0
for command in commands:
    print(commands[i])
    i = i+1

# question4
name = "Rajeev"
age = 40
print(f"Myname is {name} and I am {age} years old")

# question5
sentence = "Life is Beautiful"
print(sentence.lower())

# question6
greeting = "Hello, John!"
print(greeting.replace("John","Rajeev"))

#Question7
print(f"lenght of name is {len(name)}")

#Question8
sent2: input("Enter sentence: ")

#question9
msg = "Hello, World!"
print(msg.replace("o","e"))

#Question11
num1 = 10
num2 = 20
print(num1+num2, num2-num1, num2/num1, num1*num2)
#Question12
num3 = 30
average_list = [ num1,num2,num3]
average = sum(average_list)/len(average_list)
print(average)

#Question13
print(len(average_list))
#Question14
fruits = ["apple","banana","mango"]
print(fruits)
#Question15
numbers=[10,20,30]
numbers[1]=50
print(numbers)
#Question16
shopping_list=[]
for i in range(0,3):
    item = input("Enter your Item: ")
    shopping_list.append(item)
    print(shopping_list)
#Question17
numbers2=[1,2,3,4,5]
y=len(numbers2)-1
print(y)
numbers2.pop(y)
print(numbers2)
# Question18
fruits2 = ["apple", "banana", "mango", "orange"]
fruits2.remove("banana")
print(fruits2)
# Question19
details = {
"name": "Azad",
"Organization": "ABC Labs",
"Role": "Instructor",
"Domain": "CISCO"
}
print(details["Role"])
#Question 20
print(f"original dictionary is {details}")
details["Domain"]= "Juniper"
print(f"Value updated Dict is {details}")
#Question 21
details.update({"Exp":"5yrs"})
print(f"Key and Value updated dictionary is {details}")

#Question 22
del details["Domain"]
print(f"Domain Key and Value deleted dictionary is {details}")

#Question 22
contacts = {
"John": 123456789,
"Jane": 987654321,
"Tom": 456789123,
}
for keys, values in contacts.items():
    print(f"{keys} contact number is {values}")

print("Question#24")

age = int(input("Enter your age: "))
if age >= 18:
    print("you can Vote")
else:
    print(" You are a kid")

print("Question#25")

score = int(input("Enter your score: "))
if score > 89:
    print("Congratulations! You passed with distinction")
else:
    print("You need to work harder")

print("Question#26")

number = int(input("Enter a number: "))
if number > 0:
    print("This is a positive number")
elif number == 0:
    print("This is a zero")
else:
    print("This is a negative number")

print("\nQuestion#27")

temp = float(input("Enter today's Temperature: "))
if temp >= 30:
    print("today is a hot day")
elif temp <= 30:
    print("This not too hot day")
    
print("\nQuestion#28")

grade = input("Enter your grade (A|B|C): ")
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")
else:
    print("Needs improvement")