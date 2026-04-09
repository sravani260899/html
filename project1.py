#project

#culculator program

#inp:add,sub,mul,divi,oprator
#out:a+b,a-b,a*b,a/b

a=int(input("enter a value:"))
b=int(input("enter b valu:"))
oprator=input("enter oprator:")

if oprator=="+":
    print("addition:",a+b)
elif oprator=="-":
    print("sub:",a-b)
elif oprator=="*":
    print("mul:",a*b)
elif oprator=="/":
    print("divi",a/b)
else:
    print("invalide oprator")