# Created by Rushikesh Surve
import tkinter as tk
import subprocess as sp
import sys
from PIL import Image, ImageTk, ImageEnhance, ImageDraw

# Import blackjack game
import blackjack

root = tk.Tk()
root.title("Trio Games")
# root.geometry("800x600")
root.resizable(False, False)
root.config(bg="#1A1A1A") # Deep dark background

# --- Player Name Section ---
player_name_frame = tk.Frame(root, bg="#2C3E50", padx=10, pady=5)
player_name_frame.pack(fill="x", side="top")

def process_console_icon(image_path, size=(30, 30), border_width=1, border_color="white"):
    img = Image.open(image_path).convert("RGBA").resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

player_icon_img = process_console_icon("assets/Icons/console_icon.png")
player_icon = player_icon_img
player_icon_label = tk.Label(player_name_frame, image=player_icon, bg="white")
player_icon_label.pack(side="left", padx=(0, 10))

player_name_label = tk.Label(player_name_frame, text="Player: Unknown", fg="#ECF0F1", bg="#2C3E50", font=("Arial", 12, "bold"))
player_name_label.pack(side="left", expand=True, anchor="w")

edit_icon_img = Image.open("assets/Icons/edit.png").resize((20, 20), Image.LANCZOS)
edit_icon = ImageTk.PhotoImage(edit_icon_img)
save_icon_img = Image.open("assets/Icons/save.png").resize((20, 20), Image.LANCZOS)
save_icon = ImageTk.PhotoImage(save_icon_img)

player_name_entry = tk.Entry(player_name_frame, fg="#E74C3C", font=("Arial", 12), bg="#BDC3C7", width=20)

def load_player_name():
    try:
        with open("data/player_name.txt", 'r') as f:
            name = f.read().strip()
            if not name:
                name = "New Player"
            player_name_label.config(text=f"Player: {name}")
    except FileNotFoundError:
        with open("data/player_name.txt", 'w') as f:
            f.write("New Player")
        player_name_label.config(text="Player: New Player")

def toggle_edit_name():
    if player_name_label.winfo_ismapped(): # If label is visible, switch to entry
        current_name = player_name_label.cget("text").replace("Player: ", "")
        player_name_label.pack_forget()
        player_name_entry.delete(0, tk.END)
        player_name_entry.insert(0, current_name)
        player_name_entry.pack(side="left", expand=True, anchor="w")
        edit_button.config(image=save_icon)
    else: # If entry is visible, save and switch to label
        new_name = player_name_entry.get().strip()
        if not new_name:
            new_name = "Unknown"
        with open("data/player_name.txt", 'w') as f:
            f.write(new_name)
        player_name_entry.pack_forget()
        player_name_label.config(text=f"Player: {new_name}")
        player_name_label.pack(side="left", expand=True, anchor="w")
        edit_button.config(image=edit_icon)

edit_button = tk.Button(player_name_frame, image=edit_icon, command=toggle_edit_name, bg="#2C3E50", relief="flat")
edit_button.pack(side="right")

load_player_name() # Load player name on startup

# --- Main Content Frame ---
main_content_frame = tk.Frame(root, bg="#1A1A1A")
main_content_frame.pack(fill="both", expand=True, padx=20, pady=20)

# --- Game Launch Functions ---
def start_game(game_path):
    sp.Popen([sys.executable, game_path])

# --- Icon Processing Function ---
def process_icon(image_path, size=(150, 150)):
    img = Image.open(image_path).convert("RGB").resize(size, Image.LANCZOS)
    # Convert to grayscale and then back to RGB to desaturate
    img = ImageEnhance.Color(img).enhance(0.5) # Reduce saturation
    return ImageTk.PhotoImage(img)

# --- Game Icons and Buttons ---
game_icons = {}

# Create game_frame first
game_frame = tk.Frame(main_content_frame, bg="#1A1A1A")
game_frame.pack(expand=True, anchor='center')

# Cubys
game_icons["cubys"] = process_icon("assets/Icons/CubysLogo.png")
cubys_btn = tk.Button(game_frame, image=game_icons["cubys"], text="Cubys", compound="top",
                      fg="#ECF0F1", bg="#34495E", relief="flat", font=("Arial", 10, "bold"),
                      command=lambda: start_game("src/cubys_final.py"))
cubys_btn.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

# Blackjack
game_icons["blackjack"] = process_icon("assets/Icons/blackjack.png")
blackjack_btn = tk.Button(game_frame, image=game_icons["blackjack"], text="Blackjack", compound="top",
                          fg="#ECF0F1", bg="#34495E", relief="flat", font=("Arial", 10, "bold"),
                          command=lambda: blackjack.GameScreen(root)) # Direct call to Toplevel
blackjack_btn.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

# Flappy Bird
game_icons["flappybird"] = process_icon("assets/Icons/flappybird.png")
flappy_btn = tk.Button(game_frame, image=game_icons["flappybird"], text="Flappy Bird", compound="top",
                       fg="#ECF0F1", bg="#34495E", relief="flat", font=("Arial", 10, "bold"),
                       command=lambda: start_game("src/flappybird.py"))
flappy_btn.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")

# Pong
game_icons["pong"] = process_icon("assets/Icons/pong.png")
pong_btn = tk.Button(game_frame, image=game_icons["pong"], text="Pong", compound="top",
                     fg="#ECF0F1", bg="#34495E", relief="flat", font=("Arial", 10, "bold"),
                     command=lambda: start_game("src/pong.py"))
pong_btn.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")

# Tetris
game_icons["tetris"] = process_icon("assets/Icons/tetris.png")
tetris_btn = tk.Button(game_frame, image=game_icons["tetris"], text="Tetris", compound="top",
                         fg="#ECF0F1", bg="#34495E", relief="flat", font=("Arial", 10, "bold"),
                         command=lambda: start_game("src/tetris.py"))
tetris_btn.grid(row=2, column=0, padx=15, pady=15, sticky="nsew")

# Chess
game_icons["chess"] = process_icon("assets/Icons/chess.png")
chess_btn = tk.Button(game_frame, image=game_icons["chess"], text="Chess", compound="top",
                        fg="#ECF0F1", bg="#34495E", relief="flat", font=("Arial", 10, "bold"),
                        command=lambda: start_game("src/chess-game/main.py"))
chess_btn.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")

# Configure columns and rows to expand evenly
game_frame.grid_columnconfigure(0, weight=1)
game_frame.grid_columnconfigure(1, weight=1)
game_frame.grid_rowconfigure(0, weight=1)
game_frame.grid_rowconfigure(1, weight=1)
game_frame.grid_rowconfigure(2, weight=1)

root.mainloop()
