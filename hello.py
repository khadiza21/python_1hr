print ("Allah is Almighty")

# var 
a = 10
b = 34

print(a+b)

#data type int, float, string 

#take input from keyboard
firstNum = 10
secondNum = input("Enter a number: ")
print("SUM: ", firstNum+ int(secondNum)) # in py lang input will be string so need to typecast


# operators : 3 (arithmetic: (+ , -, *, /), comparator: (<, >, <=, =>),  logical:(and, or , not))


#conditional statement
age = input ("Enter your age: ")

if int(age)>30:
   print("Senior")
else:
   print("Junior")

#loop
# for i in range(start, end, skip)

for i in range(1,5): #1,2,3,4
   print(i)

for i in range(1,6,2): #1,3,5
   print(i)


# 1+3+5+.....+100=?
print ("---------------------------------------------")
sum = 0
for i in range(1,101): 
    if i%2 != 0:
       continue
    else:
       sum = sum + i 
print(sum)

print ("---------------------------------------------")
sum1 = 0
for i in range(1,101,2): 
       sum1 = sum1 + i 
print(sum1)

print ("---------------------------------------------")
# while loop
sum2 = 0
i = 1
while i < 101:
   sum2 = sum2 + i
   i = i + 2
print(sum2)


#list 
fruits = ["mango", "banana", "jack"]
print(fruits[2])
for fruit in fruits:
    print(fruit)
    
