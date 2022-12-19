import turtle

turtle.bgcolor("black")

colors=["white smoke","gold","orange","red","pink", "violet","purple","turquoise","skyblue","blue", "lightgreen","green"]


p=turtle.Pen()
p.shape("turtle")

temp=30
n=3
x=3
l=20

while n<39:
    p.pencolor(colors[(n-3)%12])
    p.left(temp)
    for i in range(n):
        p.left(360/n)
        p.forward(l)

    p.penup()
    p.goto(x,0)
    p.pendown()
    temp=(360/n - 360/(n+1))/2
    n+=1
    x+=5
    l*=1.07

turtle.done()  


