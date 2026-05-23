print ("Hello World")
print (" This is my first program")
print ("  I am learning Python")
print ("   My name is Jyptirmoy Das Surjyo")
print ("    I am 23 years old", "I am from Bangladesh")
#suppose I need two numbers and i want to sum them
num1 = 20
num2 =50
num3 =(num1+num2)
print (num3)
#suppose i need to multiply two numbers
num4 =888
num5 =485
num6 =876
num7 =(num4*num5*num6)
print (num7, "This is the result of multiplying three numbers")
num8 = num5
print (num8)
print (type(num8))
name = "jojo"
print (type(name))
age = True
Old ="@"
a = None
A,B = "2",3
print (type(age))
print (type(a))

print ((A+Old)*B)
"""next"""
myname = input("what is your name?")
print ("Hello", myname)
myage = int(input("what is your age?"))
print ("Your age is", myage)
if myage >=18:
    print ("You are eligible to vote")
elif myage <18:
    print ("You are underage")
else:
    print ("You are not eligible to vote")

red = "stop"
yellow = "wait"
green = "go"
traffic = input("what is the traffic light colour?")
if (traffic == "red"):
    print ("stop")
elif (traffic == "yellow"):
    print ("wait")
elif (traffic == "green"):
    print ("go")
else:
    print ("light is broken")

A = int(input("A : "))
B = input("M/F : ")
if ((A==1 or A==2) and G == "M"):
    print("fee is 100")
elif (A==3 or A==4 or G=="F"):
    print ("fee is 200")
elif (A==5 and G=="M"):
    print("fee is 300")
else:
    print("no fee")