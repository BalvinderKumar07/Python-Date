x=int(input("enter a number\n"))
y=1

while y<=x:
    w=open(f'.txt','a')
    z=1
    while z<=10:
        w.write(f'{y} X {z} = {y*z}\n')
        z=z+1
    y=y+1        
    



