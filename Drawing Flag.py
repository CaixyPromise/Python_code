# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

import turtle
Drawing = turtle.Screen()
Drawing.title("01编程小屋")
Drawing.bgcolor('white')
Drawing.setup(800,600)
Drawing.tracer(1)

#小人类
class Person(object):
    #小人的属性
    def __init__(self,x,y,Sub):
        self.x = x
        self.y = y
        self.Head = turtle.Turtle()
        self.Eyes = turtle.Turtle()
        self.Hands = turtle.Turtle()
        self.Legs = turtle.Turtle()
        self.Body = turtle.Turtle()
        self.Word = turtle.Turtle()
        self.Sub = Sub

#绘制头的方法
    def drawHead(self):
        self.Head.pencolor("red")
        self.Head.pensize(2)
        self.Head.speed(10)
        self.Head.up()
        self.Head.goto(self.x, self.y)
        self.Head.down()
        self.Head.circle(50*self.Sub, 360)
        self.Head.hideturtle()

#绘制眼睛的方法
    def drawEyes(self):
        eX = self.Head.xcor()-20*self.Sub
        eY = self.Head.ycor()+70*self.Sub
        self.Eyes.pencolor("red")
        self.Eyes.pensize(2)
        self.Eyes.speed(10)
        self.Eyes.up()
        self.Eyes.goto(eX,eY)
        self.Eyes.down()
        self.Eyes.right(90)
        self.Eyes.forward(40*self.Sub)
        self.Eyes.up()
        self.Eyes.left(90)
        self.Eyes.forward(40*self.Sub)
        self.Eyes.left(90)
        self.Eyes.down()
        self.Eyes.forward(40*self.Sub)
        self.Eyes.hideturtle()

#绘制身体的方法
    def drawBody(self):
        bX = self.Head.xcor()
        bY = self.Head.ycor()
        self.Body.pencolor("red")
        self.Body.pensize(2)
        self.Body.speed(10)
        self.Body.up()
        self.Body.goto(bX,bY)
        self.Body.right(90)
        self.Body.down()
        self.Body.forward(100*self.Sub)
        self.Body.hideturtle()

#绘制手的方法
    def drawHands(self):
        hX = self.Head.xcor()
        hY = self.Head.ycor()-30*self.Sub
        self.Hands.pencolor("red")
        self.Hands.pensize(2)
        self.Hands.speed(10)
        self.Hands.up()
        self.Hands.goto(hX,hY)
        self.Hands.down()
        self.Hands.forward(60*self.Sub)
        self.Hands.left(60)
        self.Hands.forward(60*self.Sub)
        self.Hands.up()
        self.Hands.goto(hX,hY-15*self.Sub)
        self.Hands.right(60)
        self.Hands.down()
        self.Hands.forward(60*self.Sub)
        self.Hands.right(60)
        self.Hands.forward(60*self.Sub)
        self.Hands.hideturtle()

#绘制腿的方法
    def drawLegs(self):
        dX = self.Head.xcor()
        dY = self.Head.ycor()-100*self.Sub
        self.Legs.pencolor("red")
        self.Legs.pensize(2)
        self.Legs.speed(10)
        self.Legs.up()
        self.Legs.goto(dX,dY)
        self.Legs.down()
        self.Legs.forward(60*self.Sub)
        self.Legs.right(120)
        self.Legs.forward(60*self.Sub)
        self.Legs.up()
        self.Legs.goto(dX,dY)
        self.Legs.down()
        self.Legs.forward(60*self.Sub)
        self.Legs.hideturtle()

#绘制整个小人的方法入口
    def draw(self):
        self.drawHead()
        self.drawEyes()
        self.drawBody()
        self.drawHands()
        self.drawLegs()

#爱心的类
class Heart(object):
    #初始化爱心的属性
    def __init__(self,x,y,Sub):
        self.x = x
        self.y = y
        self.Sub = Sub
        self.Heart = turtle.Turtle()

#绘制爱心以及文字的方法
    def draw(self):
        self.Heart.up()
        self.Heart.goto(self.x,self.y)
        self.Heart.pensize(2)
        self.Heart.pencolor("red")
        self.Heart.speed(10)
        self.Heart.fillcolor("pink")
        self.Heart.begin_fill()
        self.Heart.down()
        self.Heart.left(90)
        self.Heart.circle(26*self.Sub,180)
        self.Heart.circle(75*self.Sub,72)
        self.Heart.left(36)
        self.Heart.circle(75*self.Sub,72)
        self.Heart.circle(26*self.Sub,180)
        self.Heart.end_fill()
        self.Heart.up()
        self.Heart.forward(120*self.Sub)
        self.Heart.right(90)
        self.Heart.forward(60*self.Sub)
        self.Heart.write("伟大、光荣、正确的中国共产党万岁\n伟大、光荣、英雄的中国人民万岁",align='left',font=('Consolas',10*self.Sub,"normal"))
        self.Heart.hideturtle()

#绘制党旗的类
class PartyFlag(object):
    #初始化党旗属性
    def __init__(self,x,y,Sub):
        self.x = x
        self.y = y
        self.Sub = Sub
        self.frame = turtle.Turtle()
        self.sickle = turtle.Turtle()
        self.ax = turtle.Turtle()

#绘制党旗面的方法
    def drawFrame(self):
        self.frame.up()
        self.frame.goto(self.x,self.y)
        self.frame.pencolor("red")
        self.frame.shapesize(2)
        self.frame.speed(10)
        self.frame.fillcolor("red")
        self.frame.begin_fill()
        self.frame.down()
        self.frame.forward(300*self.Sub)
        self.frame.right(90)
        self.frame.forward(200*self.Sub)
        self.frame.right(90)
        self.frame.forward(300*self.Sub)
        self.frame.right(90)
        self.frame.forward(200*self.Sub)
        self.frame.end_fill()
        self.frame.hideturtle()

#绘制斧头的方法
    def drawAx(self):
        aX = self.frame.xcor()+25*self.Sub
        aY = self.frame.ycor()-45*self.Sub
        self.ax.up()
        self.ax.goto(aX,aY)
        self.ax.pencolor("yellow")
        self.ax.pensize(2)
        self.ax.speed(10)
        self.ax.down()
        self.ax.left(45)
        self.ax.fillcolor("yellow")
        self.ax.begin_fill()
        self.ax.forward(30*self.Sub)
        self.ax.right(90)
        self.ax.circle(10*self.Sub,90)
        self.ax.right(90)
        self.ax.forward(10*self.Sub)
        self.ax.right(90)
        self.ax.forward(15*self.Sub)
        self.ax.left(90)
        self.ax.forward(70*self.Sub)
        self.ax.right(90)
        self.ax.forward(15*self.Sub)
        self.ax.right(90)
        self.ax.forward(70*self.Sub)
        self.ax.left(90)
        self.ax.forward(10*self.Sub)
        self.ax.right(90)
        self.ax.forward(20*self.Sub)
        self.ax.end_fill()
        self.ax.hideturtle()

#绘制镰刀的方法
    def drawSickle(self):
        sX = self.frame.xcor()+30*self.Sub
        sY = self.frame.ycor()-69*self.Sub
        self.sickle.up()
        self.sickle.goto(sX,sY)
        self.sickle.pencolor("yellow")
        self.sickle.pensize(2)
        self.sickle.speed(10)
        self.sickle.fillcolor("yellow")
        self.sickle.begin_fill()
        self.sickle.right(45)
        self.sickle.down()
        self.sickle.circle(40*self.Sub,90)
        self.sickle.left(25)
        self.sickle.circle(45*self.Sub,90)
        self.sickle.right(160)
        self.sickle.circle(-45*self.Sub,130)
        self.sickle.right(10)
        self.sickle.circle(-48*self.Sub,75)
        self.sickle.left(160)
        self.sickle.circle(-7*self.Sub,340)
        self.sickle.left(180)
        self.sickle.circle(-48*self.Sub,15)
        self.sickle.right(75)
        self.sickle.forward(11*self.Sub)
        self.sickle.end_fill()
        self.sickle.hideturtle()

#绘制整个党旗的方法入口
    def draw(self):
        self.drawFrame()
        self.drawAx()
        self.drawSickle()

#绘制国旗的类
class Chinaflag:
    # 初始化国旗类的属性
    def __init__(self,x,y,Sub):
        self.x = x
        self.y = y
        self.Sub = Sub
        self.frame = turtle.Turtle()
        self.star = turtle.Turtle()
        self.Star = turtle.Turtle()

#绘制国旗面的方法
    def drawFrame(self):
        self.frame.up()
        self.frame.goto(self.x,self.y)
        self.frame.pencolor("red")
        self.frame.shapesize(2)
        self.frame.speed(10)
        self.frame.fillcolor("red")
        self.frame.begin_fill()
        self.frame.down()
        self.frame.forward(300*self.Sub)
        self.frame.right(90)
        self.frame.forward(200*self.Sub)
        self.frame.right(90)
        self.frame.forward(300*self.Sub)
        self.frame.right(90)
        self.frame.forward(200*self.Sub)
        self.frame.end_fill()
        self.frame.hideturtle()

#绘制国旗的大五角星的方法
    def draw_Star(self):
        SX = self.frame.xcor() + 20 * self.Sub
        SY = self.frame.ycor() - 45 * self.Sub
        self.Star.fillcolor("yellow")
        self.Star.pencolor("yellow")
        self.Star.shapesize(2)
        self.Star.up()
        self.Star.goto(SX,SY)
        self.Star.down()
        self.Star.begin_fill()
        for i in range(5):
            self.Star.forward(50*self.Sub)
            self.Star.right(144*self.Sub)
        self.Star.end_fill()
        self.Star.hideturtle()

#绘制小五角星的方法
    def draw_star1(self):
        sX = self.frame.xcor() + 90 * self.Sub
        sY = self.frame.ycor() - 10 * self.Sub
        self.star.fillcolor("yellow")
        self.star.pencolor("yellow")
        self.star.shapesize(2)
        self.star.up()
        self.star.goto(sX,sY)
        self.star.setheading(305)
        self.star.down()
        self.star.begin_fill()
        for i in range(5):
            self.star.forward(20)
            self.star.right(144)
        self.star.end_fill()
        self.star.hideturtle()

# 绘制小五角星的方法
    def draw_star2(self):
        sX = self.frame.xcor() + 105 * self.Sub
        sY = self.frame.ycor() - 40 * self.Sub
        self.star.fillcolor("yellow")
        self.star.pencolor("yellow")
        self.star.shapesize(2)
        self.star.up()
        self.star.goto(sX, sY)
        self.star.setheading(30)
        self.star.down()
        self.star.begin_fill()
        for i in range(5):
            self.star.forward(20)
            self.star.right(144)
        self.star.end_fill()
        self.star.hideturtle()

# 绘制小五角星的方法
    def draw_star3(self):
        sX = self.frame.xcor() + 105 * self.Sub
        sY = self.frame.ycor() - 70 * self.Sub
        self.star.fillcolor("yellow")
        self.star.pencolor("yellow")
        self.star.shapesize(2)
        self.star.up()
        self.star.goto(sX, sY)
        self.star.setheading(3)
        self.star.down()
        self.star.begin_fill()
        for i in range(5):
            self.star.forward(20)
            self.star.right(144)
        self.star.end_fill()
        self.star.hideturtle()

# 绘制小五角星的方法
    def draw_star4(self):
        sX = self.frame.xcor() + 90 * self.Sub
        sY = self.frame.ycor() - 90 * self.Sub
        self.star.fillcolor("yellow")
        self.star.pencolor("yellow")
        self.star.shapesize(2)
        self.star.up()
        self.star.goto(sX, sY)
        self.star.setheading(300)
        self.star.down()
        self.star.begin_fill()
        for i in range(5):
            self.star.forward(20)
            self.star.right(144)
        self.star.end_fill()
        self.star.hideturtle()

#绘制国旗的方法入口
    def draw(self):
        self.drawFrame()
        self.draw_Star()
        self.draw_star1()
        self.draw_star2()
        self.draw_star3()
        self.draw_star4()


if __name__ == '__main__':
    #实例化对象
    person = Person(-300,70,1)
    heart = Heart(-150,55,1)
    partyFlag = PartyFlag(50,275,1)
    chinaFlag = Chinaflag(50,50,1)
    person.draw()
    heart.draw()
    partyFlag.draw()
    chinaFlag.draw()
    Drawing.mainloop()