# def wishing():
    # print("=================")
    # print("WOLCOME TO PYTHON")
    # print("=================")
# wishing()

# ===============================================================

# def is_even():
    # if x % 2 ==0:
        # print("Is even number")
    # else:
        # print("Is not even number")
# 
# x=int(input("Enter tne number\n"))  
# is_even()   
# 
# =====================================================================

# def fun():
    # a = "local"
    # print(a)
# fun()   
# 
# =============================================================================

# a = "global"
# def fun1():
    # print(a)
# def fun2():
    # print(a)
# print("____________________________")    
# print("calling fun1() and fun2()")
# fun1()
# fun2() 
# print("__________________________________")         

# ====================================================================================

# C = 100
# print("before calling modify function'c'value is :",C)
# def modify():
#     global C
#     C = 1000
#     print("Inside function 'c' value is :" , C)
#     print("End modify()")


# modify()
# print("Outside function 'c' value is :",C) 

# ===================================================================================

# def add(a,b):
#     return "a is",a,"b is",b,"a+b=",a+b

# result = add(10,20)
# print("The sum of two values is :",result)
# print("The sum of two values is :",add(100,200))

# ====================================================================================


# def add(a,b):
#     print("Without return statemant")

# result = add(10,20)
# print("The sum of two values is :",result)
# print("The sum of two values is :",add(100,200))

# ===================================================================================

# def calc(a,b):
    # c = a+b
    # d = a-b
    # e = a*b
    # f = a/b
    # return c,d,e,f
# x = 20
# y = 10
# 
# add,sub,mul,div= calc(x,y)
# print("Add of two values :",add)
# print("sub of two values :",sub)
# print("mul of two values :",mul)
# print("div of two values :",div)

# ===================================================================================

# from unittest import result
# def calc(a,b):
#     return a+b,a-b,a*b,a/b

# x = 20
# y = 10
# result = calc(x,y)
# for i in result:
#     print(i)  

# ====================================================================================

# def tuplfun(*args):
#     mlist = []
#     for arg in args:
#         mlist.append(arg*10)
#     return tuple(mlist) 

# t = tuplfun(1,2,3)
# print("Tupl return by tuplefun is :",t)       

# ======================================================================

# def sample_func():
#     """This function print hallo world"""

#     print("hello world")
#     return


# print("Method_1")
# help(sample_func)
# print("Method_2")
# help(sample_func.__doc__)

# ====================================================================================

# from re import X


# y , z = 14,2
# def all_global():
#     global x 
#     x = y+z
#     return x

# all_global()
# print(x)

# y ,z GLOBAL VARIABLES IN MODULE

# ====================================================================================

# def fun (a,b):
#     print("fast value is :",a)
#     print("2nd value is :",b)
#     return a+b

# x = fun(10,20)
# print("addition of two number is :",x)    
    
# x= 150
# y= 15

# print(fun(x,y))

# ==========================================================================

# def fun(name):
#     print("Hello",name)

# fun(input("Enter your name:\n"))

# ==========================================================================

# def odd_even(x):
#     if (x % 2 == 0):
#         print(x ,"is even number")
#         return "thanks"

#     else:
#         print(x,"is odd number")
#         return "thanks"


# # odd_even()

# x=15
# y=85

# print(odd_even(y))

# ===============================================================================

# def fun(a,b,d):
#     print("a value is :",a)
#     print("a value is :",b)
#     print("a value is :",d)
#     print("End function")

# fun(12,45,36)

# x = 18 
# y = 36

# print(fun(x,y))

# ==============================================================================

# def add(a,b):
#     print("add of two number : ",a+b)
# def sub(a,b):
#     print("sub of two number : ",a-b)
# def mul(a,b):
#     print("mul of two number : ",a*b)
# def div(a,b):
#     print("div of two number : ",a/b) 

# x = int(input("Enter the fast numbetr: "))                
# y = int(input("Enter the 2nd numbetr: ")) 
# print("===========================")  

# add(x,y)
# sub(x,y)
# mul(x,y)
# div(x,y)

# print("===========================")


# p= 5
# d= o;o7

# print(mul(p,))


# =========================================================================

# def reqAregFun(a,b):
#     print(a,b)

# reqAregFun(12,100)
# reqAregFun(100,12)  

# ===========================================================================

# def myfun(name="balvinder kumar"):
#     print("hello",name,"Thank you")

# myfun()
# myfun("Powan pubh")    

# x= "gurpeet"

# print(myfun(x))

# ======================================================================================

# def reqArgFun(name,msg):
#     print(name,msg)

# reqArgFun(name="Balvinder,",msg="my name is balvinder.")
# reqArgFun("my name is Manpreet,","Manpreet.")

# ==================================================================================

# from resource import prlimit


# def massage():
    # print("================ Hello,walcome in program.================")
# 
# massage()   

# def massage2():
    # print("=================","thank you for use me.=================")

# massage2()
# =====================================================================================

# def sum(*n):
#     total = 0
#     for a in n:
#         total = total + a
#     print("The sum = ",total)

# sum()
# sum(10)
# sum(1,2,3)
# sum(1,2,3,4,55,6)
# massage()

# ========================================================================================

# def myFun(n,*s):
#     print(n)
#     for a in s:
#         print(a)

# print("myFun(10) output :")
# myFun(10)
# print("myFun(10,20,30,40) output :")
# myFun([20,30,10,40])
# print("myFun(10,'a',20,'b') :")
# myFun([10,'a',20,'b'])

# ===================================================================================

# def myfun(*n,s):
#     for a in n:
#         print(a)
#     print(s)

# myfun('a','b',s=100) 

# =============================================================================

# def myFun(*n,s):
#     for a in n:
#         print(a)
#     print(s)

# myFun('a','b',s=100)

# ============================================================================================

# def myFun(**n):
    # for a,b in n.items():
        # print(a," = ",b)
        # 
# print("============================")
# myFun(
    # Rno=23,
    # Name="Balvinder",
    # mask=89,
    # subject="python"
# )


# ================================================================================


# def number(a,b,e,c=100,d=200,):
    # print(a,b,c,d,e)
# 
# number(5,6,0)
# number(1,2,3,4,5)
# number(5,8,67,d=89,c=58,)  
# number(a=500,b=800,c=899,e=3)


# =============================================================================



























 