#Design a calculator which will correctly solve all the problems except the following ones :
#45*3 = 555, 56+9 = 77, 56/6 = 4
#Your programs should take operator and the two numbers as input from the user and then write the result

print("FAULTY CALCULATOR")
x = int(input("Enter your first number"))
y = int(input("Enter your second number"))
a = input()
if a=="+":
  if x==56 and y==9 :
     print("77")
  else:
     print(x+y)
if a=="-":
    print(x-y)
if a=="*":
    if x==45 and y==3:
        print("555")
    else:
        print(x*y)
if a=="/":
    if x==56 and y==6:
        print("4")
    else:
        print(x/y)


