from tkinter import *
import os
import turtle
import time
import random

### Window Setup
turtle.setup(width=700 , height = 700)
turtle.title("Snake")
turtle.bgcolor("black")


##the game
def game_start():

    screen.destroy()
        
    

    turtle.Turtle._screen = None  # force recreation of singleton Screen object after turtle.bye()
    turtle.TurtleScreen._RUNNING = True

    delay= 0.1
    
    score=0
    highscore=0
    
    
    win=turtle.Screen()
    win.title('snake game')
    win.bgcolor('light green')
    win.setup(width=700,height=700)
    win.tracer(0)#turns off screen updates

    back=turtle.Turtle()
    back.ht()
    back.penup()
    back.setx(-215)
    back.sety(-340)
    back.color("black")
    back.write("Press B to go Back", align="left", font=("Nyala",25,"bold" ))
    turtle.onkeypress(homescreen,'b')
    turtle.listen()
    
    head=turtle.Turtle()
    head.speed(0)#animate speed supposed to be zero (ins)
    head.shape('square')
    head.color('blue')
    head.penup()
    head.goto(0,0)
    head.direction='stop'
    
    food=turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(random.randint(-340,340),random.randint(-320,340))
    
    seg=[]
    
    pen=turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('purple')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,300)
    
    #functions
    def move():#direction determines motion
        if head.direction=="up":
            y=head.ycor()
            head.sety(y+20)
        if head.direction=="down":
            y=head.ycor()
            head.sety(y-20)
        if head.direction=="right":
            x=head.xcor()
            head.setx(x+20)
        if head.direction=="left":
            x=head.xcor()
            head.setx(x-20)
        
    def go_up():
        if head.direction!='down':
            head.direction="up"
    def go_down():
        if head.direction!='up':
            head.direction="down"
    def go_left():
        if head.direction!='right':
            head.direction="left"
    def go_right():
        if head.direction!='left':
            head.direction="right"

    #keyboard input results in direction of head
    win.listen()
    win.onkeypress(go_up,'Up')
    win.onkeypress(go_down,'Down')
    win.onkeypress(go_left,'Left')
    win.onkeypress(go_right,'Right')

    while True:
        win.update()


        #collision with border
        if head.xcor()>349:
            head.goto(-349,head.ycor())
        if head.xcor()<-349:
            head.goto(349,head.ycor())
        if head.ycor()>349:
            head.goto(head.xcor(),-349)
        if head.ycor()<-349:
            head.goto(head.xcor(),349)    
            
        #collision with food
        if head.distance(food)<20:
            food.goto(random.randint(-340,340),random.randint(-320,340))#moves food to random place
        
            new_seg=turtle.Turtle()
            new_seg.speed(0)
            new_seg.shape('square')
            new_seg.color(color.get())
            new_seg.penup()
            seg.append(new_seg)
            
            #speed up
            delay -=0.002
            
            #scoring
            score+=10
            
            if score>highscore:
                highscore=score
                
            pen.clear()#gets rid of prev score    
            pen.write('score: {} high score: {}'.format(score,highscore),align='center',font=('Courier',30,'normal'))    
            
        #move end seg first in reverse order 
        for i in range(len(seg)-1,0,-1):#seg[0] not included because it occupies rhe previous position of the head
            x=seg[i-1].xcor()#subtract 1 from index so that the seg occupies the position of the one in front of it
            y=seg[i-1].ycor()
            seg[i].goto(x,y)
            
        #move seg[0] to where head was
        if len(seg)>0:
            x=head.xcor()
            y=head.ycor()
            seg[0].goto(x,y)
            
        move()
    
        #body collision
        for s in seg:
            if s.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction='stop'
                for s in seg:
                    s.goto(1000,1000)#take them off the screen

                seg.clear()

                #reset score
                score=0
                pen.clear()#gets rid of prev score    
                pen.write('score: {} high score: {}'.format(score,highscore),align='center',font=('Courier',30,'normal'))
                delay= 0.1
            
    
        time.sleep(delay) #speed of loop

    win.mainloop()
##input colour
def col_inp():
    
    global screen6
    screen6 = Toplevel(screen)
    
    global color
    color=StringVar()

    
    screen6.title('color input')
    screen6.geometry('700x700')
    screen6.configure(bg="orange")
    Label(screen6, text = "ENTER A COLOR FOR YOUR SNAKE", fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
    Label(screen6, text = "").pack()
    col_entry = Entry(screen6, textvariable = color)
    col_entry.pack(padx=10,pady=10)
    Button(screen6, text = "OK", command =game_start, bg = "black",fg="orange", width = "30",padx=10,pady=10, height = "2").pack()



##for login and registration
def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  
  screen3.title("Success")
  screen3.configure(bg="black")
  screen3.geometry("700x700")
  Label(screen3, text = "Login Sucess",bg = "black",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  Button(screen3, text = "GAME START!", bg = "orange",fg="black", width = "30", height = "2", padx=50,pady=50,command=col_inp).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  
  screen4.title("Success")
  screen4.geometry("700x700")
  screen4.configure(bg="orange")
  Label(screen4, text = "Password Error",bg = "black",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  Button(screen4, text = "OK", command =delete3, bg = "black",fg="orange", width = "30", height = "2",padx=50,pady=50).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  
  screen5.title("Success")
  screen5.geometry("700x700")
  screen5.configure(bg="orange")
  Label(screen5, text = "User Not Found",bg = "black",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  Button(screen5, text = "OK", command =delete4, bg = "black",fg="orange", width = "30",padx=50,pady=50, height = "2").pack()

  
def register_user():
 
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess"+"   "+username_info, fg = "green" ,font = ("calibri", 11)).pack()
  Button(screen1, text = "game start",command=col_inp, bg = "black",fg="orange", width = "30", height = "2",padx=50,pady=50).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
        
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  
  screen1.title("Register")
  screen1.geometry("700x700")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below", fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", bg = "black",fg="orange", width = "30", height = "2",padx=50,pady=50, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  
  screen2.title("Login")
  screen2.geometry("700x700")
  Label(screen2, text = "Please enter details below to login", bg = "black",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  Label(screen2, text = "").pack()
    
  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ", fg="orange", width = "80", height = "2", font = ("Calibri", 30)).pack()
  username_entry1 = Entry(screen2,width="50", textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ", fg="orange", width = "80", height = "2", font = ("Calibri", 30)).pack()
  password_entry1 = Entry(screen2,width="50", textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", bg = "black",fg="orange", width = "30", height = "2",padx=50,pady=50,command = login_verify).pack()
  Button(screen2, text = "Button", compound=LEFT)

            
            
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("700x700")
  
  screen.title("SNAKE")
  screen.configure(bg="white")
  
  Label(text = "SIGN IN", bg = "black",fg="orange", width = "300", height = "2", font = ("Calibri", 30)).pack()
  Label(text = "").pack()
  btn1=Button(text = "Login", height = "2",bg = "black",fg="orange", width = "30",command = login,padx=50,pady=50).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2",bg = "black",fg="orange" ,width = "30", command = register,padx=50,pady=50).pack()

  screen.mainloop()





### Screen Control
def pagechange(x,y):
    
    if x<83 and x>-83 and y<33 and y>3:

        turtle.bye()
        
        
        main_screen()
        
        
        

       
    
    elif x<221 and x>179 and y<-179 and y>-201:
        turtle.clearscreen()
        turtle.bgcolor("black")
        back= turtle.Turtle()
        back.ht()
        back.penup()
        back.setx(-215)
        back.sety(300)
        back.color("cyan")
        back.write("Press B to go Back", align="center", font=("Nyala",25,"bold" ))
        turtle.onkeypress(homescreen,'b')
        turtle.listen()
        message = turtle.Turtle()
        message.ht()
        message.penup()
        message.sety(210)
        message.color("cyan")
        message.write("KC International School", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(170)
        message.write("XII-A", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(130)
        message.write("           ", align="center")
        message.sety(90)
        message.write("Computer Science Project", align="center", font=("Berlin Sans FB",33,"underline" ))
        message.sety(50)
        message.write("      ", align="center")
        message.sety(10)
        message.write("Made By:", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(-30)
        message.write("      ", align="center")
        message.sety(-70)
        message.write("Aditya Dhar", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(-110)
        message.write("Dipenshu Deep Bhat", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(-150)
        message.write("Joseph Christine Pottakkal", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(-190)
        message.write("Kaveesh Bhat", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(-230)
        message.write("Rheanca Razdan", align="center", font=("Berlin Sans FB",28,"normal" ))
        message.sety(-270)
        message.write("Sanya Mahajan", align="center", font=("Berlin Sans FB",28,"normal" ))
    elif x<-124 and x>-279 and y<167 and y>-192:
        turtle.clearscreen()
        turtle.bgcolor("black")
        back= turtle.Turtle()
        back.ht()
        back.penup()
        back.setx(-215)
        back.sety(300)
        back.color("cyan")
        back.write("Press B to go Back", align="center", font=("Nyala",25,"bold" ))
        turtle.onkeypress(homescreen,'b')
        turtle.listen()
        message = turtle.Turtle()
        message.ht()
        message.penup()
        message.color("cyan")
        message.sety(130)
        message.write("How to Play", align="center", font=("Jokerman",46,"normal" ))
        message.sety(0)
        message.write("The player uses the arrow keys to control", align="center", font=("chiller",38,"normal" ))
        message.sety(-50)
        message.write("a snake and attempts to eat items by", align="center", font=("chiller",38,"normal" ))
        message.sety(-100)
        message.write("running into them with the head of the", align="center", font=("chiller",38,"normal" ))
        message.sety(-150)
        message.write("snake. Each item eaten makes the snake", align="center", font=("chiller",38,"normal" ))
        message.sety(-200)
        message.write("longer. The player loses when the snake", align="center", font=("chiller",38,"normal" ))
        message.sety(-250)
        message.write("runs into itself.", align="center", font=("chiller",38,"normal" ))

        
def homescreen():
    turtle.clearscreen()
    turtle.bgcolor("black")
    ## Logo
    logo = turtle.Turtle()
    logo.speed(0)
    logo.ht()
    logo.penup()
    logo.setx(0)
    logo.sety(75)
    logo.color("#FF7F00")
    logo.write("Snake", align="center", font=("Matura MT Script Capitals",100,"underline" ))

    ## Info
    info = turtle.Turtle()
    info.speed(0)
    info.ht()
    info.penup()
    info.setx(200)
    info.sety(-200)
    info.color('#FF7F00')
    info.write("Info", align="center", font=("Berlin Sans FB",25,"normal" ))

    ## New Game
    newgame = turtle.Turtle()
    newgame.speed(0)
    newgame.ht()
    newgame.penup()
    newgame.sety(0)
    newgame.color('#FF7F00')
    newgame.write("New Game", align="center", font=("Berlin Sans FB",35,"normal" ))

    

    ## Quit
    leave = turtle.Turtle()
    leave.ht()
    leave.penup()
    leave.sety(-300)
    leave.color('#FF7F00')
    leave.write("Press Q to Quit", align="center", font=("Berlin Sans FB",15,"normal" ))

    turtle.onscreenclick(pagechange,1)
    turtle.onkeypress(exit,"q")
    turtle.listen()


    ##Instructions
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.ht()
    instructions.penup
    instructions.setx(-200)
    instructions.sety(-200)
    
    instructions.color('#FF7F00')
    instructions.write("Instructions", align="center", font=("Berlin Sans FB",25,"normal" ))




homescreen()
turtle.onscreenclick(pagechange,1)
turtle.onkeypress(exit,"q")
turtle.listen()
