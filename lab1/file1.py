import math as Math

# Question 1

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print(last_name+" "+first_name)

# Question 2

str_n=input("Enter a number: ")
n=int(str_n)
n2=int(str_n+str_n)
n3=int(str_n+str_n+str_n)
print(n+n2+n3)

# Question 3

print("Sample string: \n a string that you \"don't\" have to escape \n This \nis a ....... multi-line \nheredoc string --------> example")

# Question 4

r=6
volume=(4/3)*Math.pi*r**3
print(volume)

# Question 5

base=input("Enter the base of the triangle: ")
height=input("Enter the height of the triangle: ")
base=int(base)
height=int(height)
area=(1/2)*base*height
print(area)

# Question 6

n = 5

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Question 7

word = input("Enter a word: ")
print(word[::-1])

# Question 8

for i in range(0,7):
    if(i%3==0 and i!=0):
        continue
    print(i)

#Question 9

for i in range(0,50):
    if(i==0):
        f=0
        s=1
        print(s)
    else:
        t=f+s
        f=s
        s=t
        if(t>50):
          break
        print(t)

# Question 10

str_input = input("Enter a string: ")
letter_count = 0
digit_count = 0

for char in str_input:
    if char.isdigit():
        digit_count += 1
    else:
        letter_count += 1

print("Number of digits:", digit_count)
print("Number of letters:", letter_count)






