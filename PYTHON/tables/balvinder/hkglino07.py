#     def wishing():
#     print(".....................")
#     print("WELCOME TO FUNCTION")
#     print(".....................")

# wishing()    

# =============================================================================================================

# def is_even():
#     if x % 2==0:
#         print("Is even number")
#     else:
#         print("Is not odd number")

# x=int(input("Enter a number\n"))   
# is_even()      

# ================================================================================================================

# LOCAL VARIABLES

# def fun():
#     a = "local"
#     print(a)
# fun()    

# ============================================================================================================

# GLOBAL VARIABLES

# a = "global"
# def fun1():
#     print(a)
# def fun2():
#     print(a)
# print("calling fun1()and fun2()")
# fun1()        
# fun2()  
# print("...................................")      

# ============================================================================================================

# a = 10
# def fun():
#     a = a * 2
#     print(a) 
# fun()    

# =============================================================================================================

# c = 100
# print("Before calling modify function 'c' value is : ",c)
# def modify():
#     global c
#     c = 2000
#     print("Inside function 'c' value is :",c)
#     print("End modify")
# modify()
# print("Outside function 'c' value is :",c)    

# ============================================================================================================

# def add(a,b):
#     return "A is ",a,"B is ",b,"A+B =",a+b

# result = add(10,20)
# print("The sum of two value is :",result) 
# print("The sum of two velue is :",add(100,200))

# ============================================================================================================

# def calc(a,b):
#     c = a+b
#     d = a-b
#     e = a*b
#     f = a/b
#     return c,d,e,f
# x = 20
# y = 10

# add,sub,mul,div,=calc(x,y)
# print("add of two velue :",add)
# print("sub of two velue :",sub)
# print("mul of two velue :",mul)
# print("div of two velue :",div)

# ============================================================================================================

# def calc (a,b):
#     return a+b,a-b,a*b,a/b

# x=20
# y=10

# result = calc(x,y)
# for i in result:
#     print(i)

# ============================================================================================================

# def myfun(a,b,c=300,d=400):
#     print(a,b,c,d)
# myfun(3,2)
# myfun(1,2,3,4)
# myfun(d=2,a=3,b=6)

# =====================================================================================

# from re import I


# p= float(input("Enter Principal amount:\n"))
# t= float(input("Enter Time period:\n"))
# r= float(input("Enter Rate of intrest:\n"))

# si=(p*t*r)/100
# totalAmount=p+si

# print("*"*30)
# print("Intrest on amount = ",si)
# print("Total Amount = ", totalAmount)
# print("*"*30)

# =====================================================================================================================

# a = "my name is balvinder kumar and i am 21years old."

# print(a.find("Kumar"))
# print(a.index("Kumar"))

# x=a.capitalize()
# x=a.title()
# x=a.lower()
# x=a.upper()
# x=a.swapcase()
# x=a.islower()
# x=a.isupper()
# x=a.istitle()

# print(x)

# ====================================================================================================================

# a = "my name is balvinder kumar and i am 21years old."

# x=a.replace("my","he")
# print(x)

# x=a.strip()
# print(x,"and my hight 6.9inc")

# x=a.lstrip()
# print(x, "               hgfmhf              ")

# x=a.rstrip()
# print(x, "               hgfmhf              ","fygkgf")

# x=a.partition("a")
# print(x)

# x= "-".join(a)
# print(x)

# a=" "

# x=a.isspace()
# print(x)

# x=" "
# print(x)

# a="myname balvinder"
# x=a.isalpha()
# print(x)

# a="my name balvinder"
# x=a.isalpha()
# print(x)

# a="687365358"
# x=a.isdigit()
# print(x)

# a="my"
# x=a.isdigit()
# print(x)

# a="Nov15"
# x=a.isalnum()
# print(x)

# a="Nov 15"
# x=a.isalnum()
# print(x)

# a="Hello,my name balvinder"
# x=a.startswith("Hello")
# print(x)

# a="my name balvinder"
# x=a.startswith("wel",5 ,52)
# print(x)

# a="Hello,my name balvinder"
# x=a.endswith("balvinder")
# print(x)

# a="my name balvinder"
# x=a.endswith("wel",5 ,52)
# print(x)

# ========================================================================================

# a="my name balvinder"
# x=a.encode()
# print(x)


# a="balvinder"
# x=a.decode()
# print(x)

# ======================================================================================

# from datetime import datetime


# today = datetime.today()
# print("Today's date :",today)

# import datetime
# from time import strftime
# from xml.dom import minicompat
# t = datetime.datetime.today()
# r = t.date()
# p = t.time()

# print(p.hour,":",p.minute,p.strftime("%p"))

# import datetime

# t = datetime.datetime.today()
# r = t.date()
# p = t.time()``

# print(p.hour,":",p.minute,p.strftime("%p"))

# print(t.strftime("%d"),"-",t.month,"-",t.year,t.strftime("%A"),",",t.strftime("%B"))


# x = datetime.datetime.now()
# print(x.strftime("%a"))
# print(x.strftime("%A"))
# print(x.strftime("%b"))
# print(x.strftime("%B"))
# print(x.strftime("%m"))
# print(x.strftime("%y"))
# print(x.strftime("%Y"))
# print(x.strftime("%H"))
# print(x.strftime("%I"))
# print(x.strftime("%p"))
# print(x.strftime("%M"))
# print(x.strftime("%S"))
# print(x.strftime("%c"))
# print(x.strftime("%x"))
# print(x.strftime("%X"))

# from datetime import datetime

# date_string="24-may,2022"
# print("hbhbjhv=",date_string)

# date_object = datetime.strptime(date_string,"%d","%B","%Y")
# print("date_object =",date_object)

# ===================================================================================================================

def recur_factial(n):
    if n==1:
        return n 
    else:
        return n*recur_factial(n-1)
# 
num = int(input("Enter the number\n"))
if num<0:
    print("sorry, factorial does not exist for negative number")
elif num==0:
    print("the factroial fo 0 is 1=") 
else:
    print("The factroial of",num,"is",recur_factial(num))
# 
# ==============================================================================================================

# l=[]
# def sum_digits(b):
#     if (b==0):
#         return l
#     dig=b%10
#     l.append(dig)
#     sum_digits(b//10)
# n=int(input("Enter the number\n"))
# sum_digits(n)
# print(sum(l))        

# ==========================================================================================================

# def power(base, p):
#     if (p==0 or p==1):
#         return base
#     else:    
#         return(base*power(base,p-1))

# base=int(input("Enter the base\n"))
# p=int(input("Enter the power value\n"))

# print("Result:",power(base, p))

# ================================================================================================================

# from math import remainder
# from this import d


# def GCD(a,b):
#     remainder = a%b
#     if(remainder==0):
#         return b
#     else:
#         return GCD(b,remainder)

# x = int(input("Enter 1st number\n"))
# y = int(input("Enter 2nd number\n"))
# print("GCD is :", GCD(x,y))  

# ===================================================================================================================

# def fab(n):
#     if n<2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)

# fabseries = int(input("Enter the number\n"))
# for i in range(fabseries):
#     print(i, "=",fab(i))      

# ==============================================================================================================

# from itertools import count
# import string


# def check_string(string):
#     counot1={"Upper":0,"lower":0}
#     for i in string:
#         if i.isupper():
#             counot1["Upper"]+=1
#         elif i.islower():
#             counot1["lower"]+=1
#         else:
#             pass

# print("Oriinal string is :",string)
# print("No of UPPER CASE Characters :",count1["Upper"])
# print("No of lower case characters :",count1["lower"])
# check_string("Welcome in bala ji")                  

# ===============================================================================================================


















