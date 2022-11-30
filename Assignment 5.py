#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
for i in range(1500,2700+1):
    if (i%7)==0 and i%5==0:
        print(i)

#2. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5
for i in range(0,7):
    if i!=3 and i!=6:
        print(i)
    else:
        continue

#3. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead
# of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#Sample Output :
#fizzbuzz
#1
#2
#fizz
#4
#Buzz
for i in range(0,50+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#4. Write a Python program to check a triangle is equilateral, isosceles or scalene.
#Note :
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with two equal sides.
#Expected Output:
#Input lengths of the triangle sides:
#x: 6
#y: 8
#z: 12
#Scalene triangle
x,y,z=input("Enter the value of x,y,z : ").split( )
if x==y and y==z and z==x:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("Isocelus Triangle")
else:
    print("Scalene Triangle")

#5. Write a Python program to calculate the sum and average of n integer numbers (input from the user).
 #Input 0 to finish
sum=0
c=0
while True:
    n=int(input("Enter a number"))
    if n==0:
        break
    else:
        sum=sum+n
        c+=1
print("sum of all the number is " , sum)
print('average of all number is', round((sum/c),2))


#6. Write a Python program to construct the following pattern, using a nested loop number.
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999
for i in range(1,10):
    print(str(i)*i)
#or
for i in range(1,10):
    for j in range(i):
        print(i,end='')
    print()

#7. Write a Python program that counts the number of elements within a list that are greater than 30.
s=list(map(int,input("Enter the elements in list").split( )))
c=0
for i in s:
    if i > 30:
        c=c+1
print(c)

#8. Take values of length and breadth of a rectangle from user and check if it is square or not.
l=int(input("enter the length"))
b=int(input("enter the breadth"))
if l==b:
    print("It is a Square")
else:
    print("It is not a square")

#9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.
q=int(input("Enter the quantity"))
total_cost=100*q
sum=0
if total_cost>1000:
    sum=total_cost-((total_cost/100)*10)
    print("the total cost is", sum)
else:
    print("the total cost is", total_cost)

#10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
s=int(input("Enter the salary : "))
service=int(input("Enter the total number of years served"))
sum=0
if service>5:
    sum=(s/100)*10
    print('The bonus amount is',sum)
else:
    print("The employee has not served more than 5 years")

#11. A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.
n=int(input("Enter the student marks : "))
if n<25:
    print("F")
elif n in range(25,45):
    print("E")
elif n in range(45,50):
    print("D")
elif n in range(50,60):
    print("C")
elif n in range(60,80):
    print("B")
else:
    print("A")

#12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
total_classes=int(input("Enter the total number of classes : "))
attended=int(input("Enter the Number of class attended: "))
if total_classes==attended:
    print("The student has attended all the classes and has 100% attendence")
    print("Student is allowed to sit in exam")
else:
    percentage=((attended/total_classes)*100)
    print("The student has attendence of ",int(percentage),'%')
    if percentage<75:
        print("student is not allowed to sit in exam")
    else:
        print("student is allowed to sit in exam")

#13. Take 10 integers from keyboard using loop and print their average value on the screen.
total=0
c=0
for i in range(10):
    s=int(input("Enter the number"))
    total =total+s
    c=c+1
print("Average value is", (total/c))

#14. Print multiplication table of 24, 50 and 29 using loop.
s=[24,50,29]
for i in s:
    for j in range(1,11):
        print(i,'X',j,'=',i*j)
    print()

#15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.
sum,c=0,0
product=1
while True:
    n=input("Enter a value : ")
    if n.upper()=='Q':
        break
    else:
        print("press Q to quit")
        sum=sum+int(n)
        product=product*int(n)
        c=c+1
print("Average of all the numbers is",(sum/c))
print("Product of all the numbers is",product)

#16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
# Iterate over list using for loop.
n=input("Enter the total number of elements in the list : ")
li=[]
for i in  range(int(n)):
    s=int(input("Insert value in list : "))
    li.append(s)
search=int(input("Enter the search element : "))
if search not in li:
    print("The search element is not present in the list : ",li)
else:
    li.remove(search)
    print("The update list after removing the search element is : ",li)

#17. Using range(1,101), make three list,
#one containing all even numbers
#one containing all odd numbers
#One containing only prime numbers.
prime=[]
odd=[]
even=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime.append(i)
print("The list of prime number is",prime)
print("The list of even number is",even)
print("The list of odd number is",odd)

#18. From the two list obtained in previous question, make new lists, containing only numbers
# which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
odd=[]
even=[]
for i in range(1,10):
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
divide_by_4=[]
divide_by_6=[]
divide_by_8=[]
divide_by_10=[]
divide_by_3=[]
divide_by_5=[]
divide_by_7=[]
divide_by_9=[]
for i in even:
    if i%4==0:
        divide_by_4.append(i)
    if i%6==0:
        divide_by_6.append(i)
    if i%8==0:
        divide_by_8.append(i)
    if i%10==0:
        divide_by_10.append(i)
    if i%3==0:
        divide_by_3.append(i)
    if i%5==0:
        divide_by_5.append(i)
    if i%7==0:
        divide_by_7.append(i)
    if i%9==0:
        divide_by_9.append(i)
print('For even list', [
        [divide_by_4] + [divide_by_6] + [divide_by_8] + [divide_by_10] + [divide_by_3] + [divide_by_5] + [
            divide_by_7] + [divide_by_9]])
divide_by_4=[]
divide_by_6=[]
divide_by_8=[]
divide_by_10=[]
divide_by_3=[]
divide_by_5=[]
divide_by_7=[]
divide_by_9=[]
for i in odd:
    if i%4==0:
        divide_by_4.append(i)
    if i%6==0:
        divide_by_6.append(i)
    if i%8==0:
        divide_by_8.append(i)
    if i%10==0:
        divide_by_10.append(i)
    if i%3==0:
        divide_by_3.append(i)
    if i%5==0:
        divide_by_5.append(i)
    if i%7==0:
        divide_by_7.append(i)
    if i%9==0:
        divide_by_9.append(i)
print('For odd list',[[divide_by_4]+[divide_by_6]+[divide_by_8]+[divide_by_10]+[divide_by_3]+[divide_by_5]+[divide_by_7]+[divide_by_9]])

#19. From a list containing ints, strings and floats, make three lists to store them separately
li=[1,'s',2,4.0,'h','r',4,7.0]
ints=[]
strings=[]
floats=[]
for i in li:
    if type(i)==int:
        ints.append(i)
    elif type(i)==str:
        strings.append(i)
    elif type(i)==float:
        floats.append(i)
print("List of Integer",ints)
print("List of string",strings)
print("List of Float",floats)

#20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
def square(n):
    return n*n
li=[1,2,3,4]
new=[]
for i in li:
    new.append(square(i))
print("The square of the list is ", new)




