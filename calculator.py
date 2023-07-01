

num_1=int(input("Enter the 1st nymber:"))
num_2=int(input("enter the 2nd number:"))
choice=input("please select the operation + - * /")
if choice=="+":
    sum =num_1+num_2
    print("sum is:",sum)
elif choice=="-":
    diff=num_1-num_2
    print("difference is:",diff)
elif choice=="*":
    mul=num_1*num_2
    print("multiplication is:",mul)
elif choice=="/":
    div=num_1/num_2
    print("qoutiont is:",div)
else:
    print("please select correct operation from above choices")