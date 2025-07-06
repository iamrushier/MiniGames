# Created by Rushikesh Surve
import tkinter as tk
import os
import json
import random
import tkinter.font as tkfont

##### constants #####
STARTED=False
ZERO=0
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 190
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"   #Green
FOOD_COLOR = "#FF0000" #Red
BACKGROUND_COLOR = "#000000"  #Black
#####################

possible_cords=set()
for x in range(0, int((GAME_WIDTH/SPACE_SIZE))):
    for y in range(0, int((GAME_HEIGHT/SPACE_SIZE))):
        possible_cords.add((x*SPACE_SIZE,y*SPACE_SIZE))


score = ZERO
direction='down'
window=tk.Tk(className='Cuby Snake') #
window.geometry("923x575")
window.configure(bg='black')
window.resizable(False,False)#
w=window.winfo_width()
outerFrame=tk.Frame(window,bg='white',)
outerFrame.pack(fill='x',padx=14,pady=14,)
title_frame=tk.Frame(outerFrame, bg='black',height=66)
title_frame.pack(fill='x',padx=2,pady=2,)
image=tk.PhotoImage(file="assets/Icons/CubysLogo.png").subsample(3)
title_font=tkfont.Font(family='HP Simplified Hans',size=65,weight='bold')
lable1=tk.Label(title_frame,image=image,bg='black')
lable1.pack(anchor='w',side=tk.LEFT)

def remove_cubys():
    window.destroy()

return_btn=tk.Button(title_frame,bg='red',fg='yellow',font="calibri 10 bold",text="Try Other",command=remove_cubys)
return_btn.pack(side=tk.RIGHT,anchor='ne')

container2=tk.Frame(window,bg='white')
container2.pack(fill='x',padx=14,pady=0)

menu_frame=tk.Frame(container2,bg='black',height=400,width=282)
menu_frame.grid(row=0,column=1,padx=5)

score_label=tk.Label(menu_frame, text="Score:0", font=('arial',29,'bold'),fg='white',bg='black')
score_label.place(x=40, y=100,anchor='w')

High_Score_score_label=tk.Label(menu_frame, text="High Score", font=('calibri',19,'bold'))
High_Score_score_label.place(x=8, y=190,anchor='sw')
High_Score_score_label.config(width=20)

high_1=tk.Label(menu_frame, text="1.   0", font=('arial',10),anchor='w')
high_1.place(x=10, y=220,anchor='sw')
high_1.config(width=32)
high_2=tk.Label(menu_frame, text="1.   0", font=('arial',10),anchor='w')
high_2.place(x=10, y=250,anchor='sw')
high_2.config(width=32)
high_3=tk.Label(menu_frame, text="1.   0", font=('arial',10),anchor='w')
high_3.place(x=10, y=280,anchor='sw')
high_3.config(width=32)


canvas = tk.Canvas(container2, bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2,font=('helvetica',70),text="Start",fill="Green",tag='startgame')
canvas.grid(row=0,column=0)


def update_highscore(score=None):
    try:
        with open("data/cubys_highscore.txt", 'r') as f:
            highscores = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        highscores = [0, 0, 0]

    if score is not None:
        highscores.append(score)
        highscores = sorted(highscores, reverse=True)[:3]

    high_1.config(text=f"1. {highscores[0]}")
    high_2.config(text=f"2. {highscores[1]}")
    high_3.config(text=f"3. {highscores[2]}")

    with open("data/cubys_highscore.txt", 'w') as f:
        json.dump(highscores, f)
    
update_highscore()

def clear():
      global ZERO,STARTED,score
      STARTED=True
      score=ZERO
      canvas.delete(tk.ALL)
      score_label.config(text="Score:{}".format(score))
      game_play()
      
restart_button=tk.Button(menu_frame,text="Start",command=clear,font=("calibri 19 bold"))
restart_button.place(x=6,y=6,anchor='nw',)
restart_button.config(width=20,height=1)

def set_button():
    global STARTED
    if STARTED ==False:
        restart_button.config(state="normal")
    else:
        restart_button.config(state="disabled")        
       
###################
class Snake:
    def __init__(self):
        global STARTED
        STARTED =True 
        set_button()
        self.body_size = BODY_PARTS
        self.coordinates =[]
        self.squares=[]
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        for x, y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self, snake):
        tuple_convert=set(tuple(x) for x in snake.coordinates)
        check_set=possible_cords.difference(tuple_convert)
        x,y=random.choice(list(check_set))
        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def game_over():
    global snake,food,STARTED,score
    update_highscore(score)
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width()/2 , canvas.winfo_height()/2, font=('consolas',70),text="Game Over",fill="red",tag='gameover')
    STARTED=False
    set_button()

def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction=='up':
        y-=SPACE_SIZE
    elif direction=='down' :
        y+=SPACE_SIZE
    elif direction == 'left':
        x-=SPACE_SIZE
    elif direction == 'right':
        x+=SPACE_SIZE
    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        score_label.config(text="Score:{}".format(score))
        canvas.delete('food')
        food=Food(snake)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        del snake,food
        STARTED = False
        game_over()
    else:
        window.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):
    global direction
    if new_direction=='left':
        if direction!='right':
            direction=new_direction
    elif new_direction=='right':
        if direction!='left':
            direction=new_direction
    elif new_direction=='up':
        if direction!='down':
            direction=new_direction
    elif new_direction=='down':
        if direction!='up':
            direction=new_direction

def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    valid_snake=list(set(tuple(every) for every in snake.coordinates[1:]))
    for body_part in valid_snake:
        if x==body_part[0] and y== body_part[1]:
            return True
    return False


def game_play():
    global restart_button
    restart_button.config(text="Restart")
    global ZERO
    global score
    global direction
    direction='down'
    score=ZERO
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.bind('<Left>',lambda event: change_direction('left'))
    window.bind('<Right>',lambda event: change_direction('right'))
    window.bind('<Up>',lambda event: change_direction('up'))
    window.bind('<Down>',lambda event: change_direction('down'))
    snake= Snake()
    food= Food(snake)
    next_turn(snake,food)

window.mainloop()