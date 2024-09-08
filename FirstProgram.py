#Taking Input from user & printing it:-

"""name = input("name : ")
#age = int(input("age : "))
#hight = float(input("and hight is : "))
#print("my name is", name, "and my age is", age, "I'm a hight tall", hight)"""

# SYNTAX- if, elif, else example's:-

"""Light = input("light : ")
if (Light == "red") :
    print("stop")
elif (Light == "green") :
    print("go")
elif (Light == "yellow") :
    print("Look")
else:
    print("Light is broken")"""

"""marks = input("marks : ")
if (marks >= "90"):
    print("A")
elif (marks >= "80" and marks < "90"):
    print("B")
elif (marks >= "70" and marks < "80"):
     print("C")
else:
    print("D")"""

#Single line if / Ternary operator
"""food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)"""

""""food = input("food : ")
print("Sweet") if food == "cake" or food == "Jalebi" else print("Not Sweet")"""

#Celever if / Ternary Operator
"""age = int(input("age : "))
vote = ("yes","No") [age <= 18]
print(vote)"""

#even or odd
"""num = int(input("enter number: "))
if (num % 2 == 0):
    print("even"),
else:
    print("odd")"""

#find the greater number
"""a = int(input("fir num: "))
b = int(input("sec num: "))
c = int(input("thir num: "))
if (a >= b and a >= c):
    print(a),
elif (b >= c):
    print(b),
else:
    print(c)"""

#multiple of number
"""num = int(input("enter num: "))
if (num % 7== 0):
    print("It is"),
else:
    print("It is not")"""

#change a str into list form via apends
"""movies = []
movies.append(input("movies1 : "))
movies.append(input("movies2 : "))
movies.append(input("movies3 : "))
print(movies)"""

#Loop
#V = 1
#while V <= 10 :
    #print("v", V)
    #V += 1

#for table (loop)
#n = int(input("enter number : "))
#i = 1
#while i <= 10 :
    #print(n*i)
    #i += 1

#for index (loop)
#nums = [3, 200, 33, 98, 76, 65, 76, 00, 400]
#idx = 0
#while idx < len(nums):
    #print(nums[idx])
    #idx += 1

#loop for index
#nums = [3, 200, 33, 98, 76, 65, 76, 00, 400]
#x = int(input("enter_number :"))
#idx = 0
#while idx < len(nums):
    #if(nums[idx] == x):
        #print ("your number is found", idx)
        #idx += 1

#break in loop
"""i = 1
while i <= 10:
    print(i)
    if(i == 7):
        break
    i += 1"""

#add all number between 1 to 5(for loop)
"""n = 5
sum = 0
for i in range (1, n+1):
    sum += i
    print("total =",sum)"""

#factor any number (while loop)
"""n=4
fact=1

for i in range (1, n+1):
    fact *= i

    print ("ans =", fact)"""

#sum any number(Function)
"""def calc_sum (a, b):
    sum = a+b
    print(sum)
    return sum

calc_sum(34,56)
calc_sum(4049,8203)"""

#second method(function)
"""def calc_sum (a,b,c):
    return (a+b+c)
sum=calc_sum(29,90,54)
print(sum)"""

#def print_hello ():
    #print ("hello")
"""print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()"""

#avg of 3 number(Function)
"""def avg_no(a,b,c):
    return(a+b+c/3)
avg=avg_no(2,1,3)
print(avg)"""

#waf to def len of list parameter
"""god=["Hanuman","Shiva","Ganesh","Ma Durga","Krishna","Vishnu"]
Name=["vickey","kumar","sahil","om","vikas"]
AtoZ=["a","b","c","d"]
def print_len(list):
    print(len(list))

print_len(Name)
print_len(AtoZ)
print_len(god)"""

#convert USD into INR(function)

#def coverter(usd_val):
    #inr= (usd_val *80)
    #print("usd =",inr,"INR")
#coverter(10)

#odd and even find (function)

#def find(number):
 #   if (number%2 == 0):
  #      print("even")
   # else:
    #    print("odd")
#find(9)

#recursion function
"""def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)


show(10)"""

#factor on every number(recursion)

#def fact(n):
"""   if(n == 0 or n == 1):
        return 1
    return fact(n-1) +n
    
print(fact(4))"""

#using list and indx in recursion
#def print_list(list, idx=0):
#    if (idx== len(list)):
#        return
#    print(list[idx])
#    print_list(list, idx+1)
#list=("vickey","sameer","rahul","sam","maggie","ryan","adhrew")
#print_list(list)

#file i/o to read a file

