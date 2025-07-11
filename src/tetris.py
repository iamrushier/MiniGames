
import tkinter as tk
import random
from ShapeClasses import *

# Game constants
GAME_WIDTH = 300
GAME_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = GAME_WIDTH // GRID_SIZE
GRID_HEIGHT = GAME_HEIGHT // GRID_SIZE
SPEED = 500

# Colors
BACKGROUND_COLOR = "#000000"
GRID_COLOR = "#404040"

class TetrisGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tetris")
        self.master.configure(bg=BACKGROUND_COLOR)
        self.master.resizable(False, False)

        instructions_text = " Move : ← , → | Rotate : ↑ | Drop : ↓ "
        self.instructions_label = tk.Label(self.master, text=instructions_text, fg="white", bg=BACKGROUND_COLOR, font=("Helvetica", 12))
        self.instructions_label.pack(pady=5)

        self.canvas = tk.Canvas(self.master, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=1, highlightbackground="white")
        self.canvas.pack()

        self.score_label = tk.Label(self.master, text="Score: 0", fg="white", bg=BACKGROUND_COLOR, font=("Helvetica", 16))
        self.score_label.pack(pady=5)

        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.draw_grid()

        self.start_game()

    def draw_grid(self):
        self.canvas.delete("grid")
        for i in range(GRID_WIDTH):
            self.canvas.create_line(i * GRID_SIZE, 0, i * GRID_SIZE, GAME_HEIGHT, fill=GRID_COLOR, tags="grid")
        for i in range(GRID_HEIGHT):
            self.canvas.create_line(0, i * GRID_SIZE, GAME_WIDTH, i * GRID_SIZE, fill=GRID_COLOR, tags="grid")

        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x] != 0:
                    self.canvas.create_rectangle(x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE, fill="blue", tags="grid")

    def start_game(self):
        self.score = 0
        self.game_over = False
        self.current_piece = self.new_piece()
        self.draw_piece()
        self.game_loop()

    def new_piece(self):
        shape_class = random.choice([I, J, L, O, S, T, Z])
        piece = shape_class()
        piece.x = GRID_WIDTH // 2
        piece.y = 0
        piece.position = 0
        self.update_piece_coords(piece)
        return piece

    def update_piece_coords(self, piece):
        rotate_method = getattr(piece, f"position_{piece.position}")
        rotate_method(piece.x, piece.y)

    def draw_piece(self):
        self.canvas.delete("piece")
        for (x, y) in self.current_piece.coordinates:
            if y >= 0:
                self.canvas.create_rectangle(x * GRID_SIZE, y * GRID_SIZE,
                                             (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
                                             fill="cyan", tags="piece")

    def game_loop(self):
        if not self.game_over:
            self.move_down()
            self.master.after(SPEED, self.game_loop)

    def move_down(self):
        if not self.check_collision(self.current_piece.x, self.current_piece.y + 1, self.current_piece.position):
            self.current_piece.y += 1
            self.update_piece_coords(self.current_piece)
        else:
            self.lock_piece()
        self.draw_piece()

    def move_left(self, event):
        if not self.check_collision(self.current_piece.x - 1, self.current_piece.y, self.current_piece.position):
            self.current_piece.x -= 1
            self.update_piece_coords(self.current_piece)
            self.draw_piece()

    def move_right(self, event):
        if not self.check_collision(self.current_piece.x + 1, self.current_piece.y, self.current_piece.position):
            self.current_piece.x += 1
            self.update_piece_coords(self.current_piece)
            self.draw_piece()

    def rotate_piece(self, event):
        if isinstance(self.current_piece, O):
            return

        next_position = (self.current_piece.position + 1) % 4
        
        if not self.check_collision(self.current_piece.x, self.current_piece.y, next_position):
            self.current_piece.position = next_position
            self.update_piece_coords(self.current_piece)
            self.draw_piece()

    def hard_drop(self, event):
        while not self.check_collision(self.current_piece.x, self.current_piece.y + 1, self.current_piece.position):
            self.current_piece.y += 1
        self.update_piece_coords(self.current_piece)
        self.lock_piece()
        self.draw_piece()

    def check_collision(self, x, y, position):
        temp_piece = self.current_piece.__class__()
        rotate_method = getattr(temp_piece, f"position_{position}")
        rotate_method(x, y)
        
        for (px, py) in temp_piece.coordinates:
            if not (0 <= px < GRID_WIDTH and py < GRID_HEIGHT):
                return True
            if py >= 0 and self.grid[py][px] != 0:
                return True
        return False

    def lock_piece(self):
        for (x, y) in self.current_piece.coordinates:
            if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                self.grid[y][x] = 1
        self.clear_lines()
        self.current_piece = self.new_piece()
        if self.check_collision(self.current_piece.x, self.current_piece.y, self.current_piece.position):
            self.game_over = True
            self.canvas.create_rectangle(0, 0, GAME_WIDTH, GAME_HEIGHT, fill="black", stipple="gray50", tags="gameover_screen")
            self.canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 40, text="Game Over", fill="red", font=("Helvetica", 40, "bold"), tags="gameover_screen")
            self.canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 20, text=f"Your Score: {self.score}", fill="white", font=("Helvetica", 20), tags="gameover_screen")
            self.canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 70, text="Press 'R' to Restart", fill="white", font=("Helvetica", 16), tags="gameover_screen")
            self.canvas.tag_raise("gameover_screen")
        else:
            self.draw_grid()

    def clear_lines(self):
        lines_cleared = 0
        new_grid = [row for row in self.grid if not all(row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        if lines_cleared > 0:
            self.score += lines_cleared * 10
            self.score_label.config(text=f"Score: {self.score}")
            for _ in range(lines_cleared):
                new_grid.insert(0, [0] * GRID_WIDTH)
            self.grid = new_grid

    def restart_game(self, event=None):
        if self.game_over:
            self.canvas.delete("gameover_screen")
            self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
            self.draw_grid()
            self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TetrisGame(root)
    root.bind("<Left>", game.move_left)
    root.bind("<Right>", game.move_right)
    root.bind("<Up>", game.rotate_piece)
    root.bind("<Down>", game.hard_drop)
    root.bind("<r>", game.restart_game)
    root.mainloop()
