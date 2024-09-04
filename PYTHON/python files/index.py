
y=5
x=1

while x<=y:
    w=open(f'.txt','a')
    z=1
    while z<=10:
        w.write(f'{z} * {x} = {x*z}\n')
        z=z+1
    x=x+1
