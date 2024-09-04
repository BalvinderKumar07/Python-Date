# x=1
# y=2

# print(x+y)

# name="balvinder"
# fname="pala ram"
# address="""akanwali,
# tohona,
# haryana"""

# print(name)           
# print(fname)           
# print(address)           

# pyC=1+2j
# print(type(pyC))

# bset={4,5,69,48,69,12,4}

# print(bset)
# bset.pop()
# bset.remove(11)
# bset.discard(9)
# bset.add(555)
# bset.update(["84"])

# print(bset)

# no="123456789045"

# print(no)
# print(no[:4])
# print(no[::5])

# x=("56","45","78","45")

# for item in x:
#   print(item+"***")
# ============================================================================================
# name=input("Enter of the student\n")
# age=int(input("Enter age of the student\n"))
# address=input("Enter address of the student\n")

# print=("================================")
# print=("name: {}\nage: {}\naddress: {}".format(name,age,address))

# ============================================================================================

# n1=int(input("Enter any number\n"))
# n2=int(input("Enter any number\n"))
# n3=int(input("Enter any number\n"))

# sum=n1+n2+n3
# average=sum/3

# print("sum of three number is:",sum)
# print("average of three number is:",average)

# ===========================================================================================

# PI=3.14
# radius=float(input("Enter the radius of a circle\n"))

# area=PI*radius*radius
# circumference=2*PI*radius

# print("area of the circle=%.2f"%area)
# print("circumference of a circle =%.2f"%circumference)

# ============================================================================================

# import math
# name=float(input("Enter the cirumfercene of a circle:\n"))

# area=(name*name)/(4 *math.pi)

# print("Area of a cricle=%.2f" %area)

# ===========================================================================================
# x=int(input("Enter the number\n"))
# y=1

# while y<=x:
#     print(y)
#     y=1+y
# 
# ====================================================================================

# y=int(input("Enter any number\n"))
# x=0
# # print("Enter while loop")
# while x<=y:
#     print(x)
#     x=x+1
# print("Exit the loop ")

# =======================================================================================

# val=int(input("Enter any number\n"))

# sum=0
# i=1
# while i<=val:                     
#     sum=sum+i
#     i=i+1
# print("The sum is",sum)

# ==================================================================================

# x=int(input("Enter any number\n"))
# y=1
# sumeven=sumodd=0

# while (y<=x):
#     if(y%2)==0:
#         sumeven+=y
#     else:
#         sumodd+=y
#     y+=1
#     print("sum of the enev number up to",x,"is",sumeven)        
#     print("sum of the odd number up to",x,"is",sumodd)        

# =======================================================================================

# x=int(input("Enter any number\n"))
# fact=1
# y=1

# while(y<=x):
#     fact=fact*y
#     y=y+1
# print("the foctoial is ",fact)

# ===========================================================================================

# from re import X

# rov=0
# num=int(input("Enter any number\n"))
# n=num

# while (num):
#     rem=num%10
#     rev=rev*10+rem                               
#     num//=10
# print("Revers of number is :",rev)
# if n==rev:
#     print("palindrome")
# else:
#     print("not palindrome ")

# ========================================================================================

# n=int(input("Enter the number\n"))

# while n>0:
#     n-=1
#     print(n)

# ======================================================================================
# x=[12,45,78,65,96]
# for item in x :
#     print(x)

# ====================================================================================

# for i in range(1,100,2):
#     print(i , end=",")

# ====================================================================================

# sum=0
# for i in range(0,11,2):
#     sum=sum+i
#     # print("Sum of the even number<=",i,"is" ,sum)
#     print(sum)

# =========================================================================================

# for i in range

# n=int(input("Enter the any number\n"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# ============================================================================================

# n=int(input("Enter the any number\n"))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("* "*i)

# ==========================================================================================

# n=int(input("Enter the any number\n"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i) 

# =====================================================================================

# for row in range(6):
#     for col in range(6):
#         if col==0 or col ==5 or (row == col and col>0 and col<5):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()            

# ==========================================================================================

# x=int(input("Enter the any number\n"))
# y=1

# while y<=x:
#     print(x)
#     y=y+1

# =====================================================================================
# x='python'
# for i in x:
#     print(i,end=',')
# else:
#     print("for loop over")    

# ========================================================================

# i = 0
# while i<=10:
#     print(" i:",i)
#     if (i==4):
#         break
#         i=i+1
# print("After while loop")
# #
# =================================================================================

# for i in range(10):
#     print("i value :",i)
#     if (i==4):
#         break
# print("After for loop")

# ====================================================================================

# for i in "python":
#     if (i=="0"):
#         break
#     print(i)
# print("After for loop")   
# 
# ==============================================================================
 
# a = 0
# while a<=10:
#     if a==4:
#         break
#     a=a+1
#     print(a)
# else:
#     print("success")    

# ==========================================================================================

# for a in 'python':
#     if a =='h':
#         continue
#     else:
#         print('current Letter:',a)
# print("good bye!")

# ======================================================================================

# var=10
# while var>0:
#     var=var-1
#     if var ==5:
#      continue
#     print("crunet  :",var)
# print("good bye!")   
# 
# =========================================================================================
 
# for a in "python":
#     if a == "h":
#         pass
#         print("this is pass block")
#     print("current letter :",a)
# print("Good bye!")        
# 

# ====================================================================================

# x=int(input("Enter any number\n"))
# y=1

# while y<=x:
#     print(y)
#     y=y+1
# else:
#     print("loop is end")    

# ================================================================================

# n=int(input("Enter any number\n")) 
# sum=0
# for i in range(10,n):
#     if (n%i==0):
#         print("The number is perfact")
#         sum=sum+1
        
# if (sum==n):
#     print("The number is perfact")
# else:
#     print("tne number is not perfact")            

# ================================================================================================================

# n=int(input("Enter the number which you want a factor\n"))
# print("the factor of ",n,"are :")
# for i in range (1,n+1):
#     if n%i==0:
#         print(i)

# =====================================================================================================

# n=int(input("Enter the any number\n"))
# for i in range(n,0,-1):
#     print((n-i)*" "+i*"*")

# =======================================================================================================

# number=int(input("Enter any number\n"))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range (1,number):
#     n3=n1+n2
#     print(n3)
#     n1,n2=n2,n3

# =============================================================================================================

n=int(input("Enter the  number for \n"))
x=int(input("Enter any number\n"))
y=1
even=0

while (y<=x):
    if x%2==0:
        even=even+y
        y=y+1
print(even)    
   

   
