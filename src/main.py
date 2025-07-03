# Created by Rushikesh Surve
import tkinter as tk
import subprocess as sp
import sys
from PIL import Image,ImageTk
import blackjack
root=tk.Tk()
root.title("Trio Games")
root.config(bg='white')
root.geometry("800x600")
root.resizable(False,False)

IS_LABEL=True

def start_cubys():
    sp.Popen([sys.executable, "src/cubys_final.py"])
def start_flappybird():
    sp.Popen([sys.executable, "src/flappybird.py"])
def start_pong():
    sp.Popen([sys.executable, "src/pong.py"])

def start_blackjack():
    game = blackjack.GameScreen(root)


try:
    contents=open("data/player_name.txt",'r+')
except FileNotFoundError:
    contents=open("data/player_name.txt",'w')
    contents.write("New Player")
    contents.close() 
content=open("data/player_name.txt",'r+')
player_name=content.read()
content.close()

name_frame=tk.Frame(root,bg='white',)
name_frame.pack(fill='x')
content_frame=tk.Frame(root,bg='black',)
content_frame.pack(fill='both',expand=True,padx=5,pady=2.5)
text_label = tk.Label(name_frame, text='TRIO GAMES', fg='red', bg='black',height=2,font=("Jokerman 36 bold"))
text_label.pack(fill='x',padx=5,pady=5)

option_frame=tk.Frame(content_frame,bg='white',)
option_frame.pack(fill='both',side=tk.LEFT,padx=5,pady=5)


#cubys_logo=tk.PhotoImage(file='CubysLogo.png')
#cubys_logo=cubys_logo.subsample(3,3)

cubys_logo=Image.open("assets/Icons/CubysLogo.png")
cubys_logo=cubys_logo.resize((300,160),Image.LANCZOS)
cubys_logo=ImageTk.PhotoImage(cubys_logo)

#pong_logo=tk.PhotoImage(file=' Gallery/pong.png')
#pong_logo=pong_logo.subsample(2,2)
pong_logo=Image.open("assets/Icons/pong.png")
pong_logo=pong_logo.resize((150,150),Image.LANCZOS)
pong_logo=ImageTk.PhotoImage(pong_logo)

#flappy_logo=tk.PhotoImage(file='Gallery/flappybird.png')
#flappy_logo=flappy_logo.subsample(2,2)
flappy_logo=Image.open("assets/Icons/flappybird.png")
flappy_logo=flappy_logo.resize((150,150),Image.LANCZOS)
flappy_logo=ImageTk.PhotoImage(flappy_logo)

blackjack_logo=Image.open("assets/Icons/blackjack.png")
blackjack_logo=blackjack_logo.resize((150,150),Image.LANCZOS)
blackjack_logo=ImageTk.PhotoImage(blackjack_logo)
mini_frame=tk.Frame(option_frame,bg='white',)
mini_frame.pack(fill='x',side=tk.TOP,padx=2,pady=2)

player_icon=tk.PhotoImage(file='assets/Icons/p2.png')
player_icon=player_icon.subsample(4,4)
icon_label=tk.Label(option_frame,image=player_icon)
icon_label.pack(fill='x',side=tk.TOP)

edit_icon=tk.PhotoImage(file='assets/Icons/edit.png')
edit_icon=edit_icon.subsample(5,5)

save_icon=tk.PhotoImage(file='assets/Icons/save.png')
save_icon=save_icon.subsample(5,5)

name_frame=tk.Frame(option_frame,bg='white',)
name_frame.pack(fill='x',side=tk.TOP,padx=2,pady=2)

name_label = tk.Label(name_frame,text=player_name,fg='Black',font="arial 10 bold",bg='grey',width=25)
name_label.pack(side=tk.LEFT,fill='x',padx=2,expand=True)
name_box=tk.Entry(name_frame,text=player_name,fg='Red',font="arial 10",bg='light grey',width=30)

  



def change_name():
    global name_box,name_label,IS_LABEL
    if IS_LABEL==True:
      player_name=name_label.cget("text")
      name_label.destroy()    
      name_box=tk.Entry(name_frame,text=player_name,fg='Red',font="arial 10 bold",bg='light grey',width=30)
      name_box.pack(fill='x',side=tk.LEFT,expand=True,padx=2)
      edit_btn.config(image=save_icon)  
      IS_LABEL=False	
    else:
      player_name=name_box.get()
      content=open("data/player_name.txt",'w')
      if player_name.strip()=="":
        player_name="Unknown"
      content.write(player_name)
      content.close()
      name_box.destroy()
      name_label = tk.Label(name_frame,text=player_name,fg='Black',font="arial 10 bold",bg='grey',width=25)
      name_label.pack(side=tk.LEFT,fill='x',padx=2,expand=True)
      edit_btn.config(image=edit_icon)
      IS_LABEL=True

edit_btn=tk.Button(name_frame,bg='light grey',fg='black',width=20,height=20,image=edit_icon,command=change_name)
edit_btn.pack(side=tk.RIGHT,)

button_frame=tk.Frame(content_frame,bg='black',)
button_frame.pack(fill='both',expand=True,side=tk.LEFT)
top_btn_frame=tk.Frame(button_frame,bg='white')
top_btn_frame.pack(fill='both',expand=True,side=tk.TOP,padx=5,pady=5)
bottom_btn=tk.Frame(button_frame,bg='white')
bottom_btn.pack(fill='both',expand=True,side=tk.BOTTOM,padx=5,pady=5)

pong_btn=tk.Button(top_btn_frame,image=pong_logo,bg='black',fg='white',command=start_pong)
pong_btn.pack(fill='both',expand=True,padx=20,pady=20,side=tk.LEFT,anchor=tk.NW)

flappy_btn=tk.Button(top_btn_frame,image=flappy_logo,bg='black',fg='white',command=start_flappybird)
flappy_btn.pack( fill='both',expand=True, padx=20,pady=20,side=tk.LEFT,anchor=tk.NE)

blackjack_btn=tk.Button(top_btn_frame,image=blackjack_logo,bg='black',fg='white',command=start_blackjack)
blackjack_btn.pack( fill='both',expand=True, padx=20,pady=20,side=tk.LEFT,anchor=tk.NE)

cubys_btn=tk.Button(bottom_btn,width=20,image=cubys_logo,command=start_cubys,bg='black',fg='white')
cubys_btn.pack(fill='both',expand=True,padx=20,pady=20,side=tk.BOTTOM,)

icon_label = tk.Label(mini_frame,text="Menu",fg='white',font="arial 10 bold",bg='black',width=30,relief='sunken')
icon_label.pack()
root.mainloop()