x=20

def summ():
    global x
    x=10
    x=30
    def yy():
        nonlocal 
        x=x+5
        x=10
        print(x)
    yy()
summ()
