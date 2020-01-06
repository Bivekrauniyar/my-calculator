print("welcome to my calculator\n made by bivek" )
print("enter your operator",
      "+","-","*","/","%")
n1=input()
print("enter first number")
n2=input()
print("enter second number")
n3=input()
if n1=="+":
    print(int(n2)+int(n3))
elif n1=="-":
    print(int(n2)-int(n3))
elif n1=="*":
        print(int(n2)*int(n3))
elif n1=="/":
    print(int(n2)/int(n3))
elif n1=="%":
    print(int(n2)%int(n3))
print("thanks")



