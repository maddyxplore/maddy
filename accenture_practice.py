"""
You are required to write the code. You can click on compile & run anytime to check the compilation/ execution status of the program. The submitted code should be logically/syntactically correct and pass all the test cases.

Ques: The program is supposed to calculate the distance between three points.

For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6

Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2

ans:
"""
x1,y1 = 1,1
x2,y2 = 2,4
x3,y3 = 3,6

def sqrt(x,y,x1,y1):
    res = (((y-x)**2) + ((y1-x1)**2))**0.5
    return int(res)

print(sqrt(x1,y1,x2,y2),sqrt(x2,y2,x3,y3),sqrt(x3,y3,x1,y1))

# Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate pallindrome numbers.

x,y = 10,80

for i in range(x,y):
    reverse = 0
    temp = i
    while (temp != 0):
        remainder = temp%10
        reverse = (reverse*10)+remainder
        temp = temp // 10
    if i == reverse:
        print(reverse,end=" ")

# Problem: Write a program in C to display the table of a number and print the sum of all the multiples in it.

n = 5
table,total = [],0
for i in range(1,11):
    table.append(i*n)
    total+=(i*n)
print(*table)
print(total)        

#You are required to input the size of the matrix then the elements of matrix, then you have to divide the main matrix in two sub matrices (even and odd) in such a way that element at 0 index will be considered as even and element at 1st index will be considered as odd and so on. then you have sort the even and odd matrices in ascending order then print the sum of second largest number from both the matrices

n = int(input("Enter the number: "))
odd,even = [],[]

for i in range(n):
    temp = int(input("Enter the {} element".format(i)))
    if i%2==0:
        even.append(temp)
    else:
        odd.append(temp)
odd.sort()
even.sort()

print(*odd)
print(*even)
print(odd[-2]+even[-2])

#The function accepts 2 positive integer ‘m’ and ‘n’ as its arguments.You are required to calculate the sum of numbers divisible both by 3 and 5, between ‘m’ and ‘n’ both inclusive and return the same.
m = int(input())
n = int(input())

sum = 0

for i in range(m,n+1):
    if i%3==0 and i%5==0:
        sum+=i
print(sum)

#You have to find and return the number between ‘a’ and ‘b’ ( range inclusive on both ends) which has the maximum exponent of 2.
#a,b = int(input()), int(input())
a,b = 7,12
def expo(n):
    temp = 0
    while(n%2==0 and n!=0):
        temp+=1
        n//=2
    return temp
max = 0
temp = 0
for i in range(a,b+1):
    if expo(i)>temp:
        temp = expo(i)
        max = i

print(max)

#The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return.
c = int(input("Enter the choice 1 to 4: "))
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
def calc(c,a,b):
    if c==1:return a+b
    elif c==2:return abs(a-b)
    elif c==3:return a*b
    elif c==4:return a/b
    else:return("Enter the option from 1 to 4")
print(calc(c,a,b))

#
