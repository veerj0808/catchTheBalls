import tkinter as tk
import random

class CatchBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch The Balls!")
        self.root.geometry("600x500")

        self.score = 0
        self.time_left = 20
        self.game_running = False
        self.ball = []

        # ---------- START SCREEN ----------
        self.start_frame = tk.Frame(root)
        self.start_frame.pack(expand=True)

        tk.Label(self.start_frame, text="CATCH THE Balls!", font=("Arial", 28)).pack(pady=20)

        tk.Button(self.start_frame, text="Start Game", font=("Arial", 18),
                  command=self.start_game).pack(pady=10)
        tk.Button(self.start_frame, text="Quit", font=("Arial", 18),
                  command=root.quit).pack()

        # ---------- GAME SCREEN ----------
        self.game_frame = tk.Frame(root)

        # Score
        self.score_label = tk.Label(self.game_frame, text="Score: 0", font=("Arial", 16))
        self.score_label.grid(row=0, column=0, padx=10)

        # Timer
        self.timer_label = tk.Label(self.game_frame, text="Time: 20", font=("Arial", 16))
        self.timer_label.grid(row=0, column=1, padx=10)

        # Pause/Resume
        self.pause_button = tk.Button(self.game_frame, text="Pause", font=("Arial", 14),
                                      command=self.pause_resume_game)
        self.pause_button.grid(row=0, column=2, padx=10)

        # Canvas
        self.canvas = tk.Canvas(self.game_frame, width=550, height=400, bg="lightyellow")
        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)

        # Player basket
        self.basket_width = 100
        self.basket = self.canvas.create_rectangle(
            250, 360, 350, 380, fill="brown"
        )

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # ---------- END SCREEN ----------
        self.end_frame = tk.Frame(root)

    # ------------------------------------------------------------
    # Start Game
    # ------------------------------------------------------------
    def start_game(self):
        self.start_frame.pack_forget()
        self.end_frame.pack_forget()

        self.score = 0
        self.time_left = 20
        self.game_running = True
        self.ball.clear()
        self.canvas.delete("all")

        # redraw basket
        self.basket = self.canvas.create_rectangle(
            250, 360, 350, 380, fill="brown"
        )

        self.score_label.config(text="Score: 0")
        self.timer_label.config(text="Time: 20")
        self.pause_button.config(text="Pause")

        self.game_frame.pack()
        self.spawn_ball()
        self.update_ball()
        self.update_timer()

    # ------------------------------------------------------------
    # Pause / Resume
    # ------------------------------------------------------------
    def pause_resume_game(self):
        if self.game_running:
            self.game_running = False
            self.pause_button.config(text="Resume")
        else:
            self.game_running = True
            self.pause_button.config(text="Pause")
            self.spawn_fruit()
            self.update_fruits()
            self.update_timer()

    # ------------------------------------------------------------
    # Player Movements
    # ------------------------------------------------------------
    def move_left(self, event):
        if self.game_running:
            self.canvas.move(self.basket, -60, 0)

    def move_right(self, event):
        if self.game_running:
            self.canvas.move(self.basket, 60, 0)

    # ------------------------------------------------------------
    # Spawn Fruits
    # ------------------------------------------------------------
    def spawn_ball(self):
        if not self.game_running or self.time_left <= 0:
            return

        x = random.randint(20, 520)
        ball = self.canvas.create_oval(x, 10, x+30, 40,
                                        fill=random.choice(["red", "orange", "green", "purple"]))
        self.ball.append(ball)

        self.root.after(700, self.spawn_fruit)

    # ------------------------------------------------------------
    # Update Fruits (falling)
    # ------------------------------------------------------------
    def update_ball(self):
        if not self.game_running:
            return

        basket_coords = self.canvas.coords(self.basket)

        to_remove = []

        for ball in self.ball:
            self.canvas.move(ball, 0, 7)
            ball_coords = self.canvas.coords(ball)

            # Check if caught
            if ball_coords[3] >= basket_coords[1]:  # bottom of fruit touches basket top
                if basket_coords[0] < ball_coords[0] < basket_coords[2]:
                    to_remove.append(ball)
                    self.score += 1
                    self.score_label.config(text=f"Score: {self.score}")
                else:
                    to_remove.append(ball)  # missed

            # Remove if off screen
            if ball_coords[3] > 420:
                to_remove.append(ball)

        # Cleanup
        for fruit in to_remove:
            if fruit in self.fruits:
                self.fruits.remove(ball)
            self.canvas.delete(ball)

        self.root.after(50, self.update_fruits)

    # ------------------------------------------------------------
    # Timer
    # ------------------------------------------------------------
    def update_timer(self):
        if not self.game_running:
            return

        if self.time_left <= 0:
            self.end_game()
            return

        self.time_left -= 1
        self.timer_label.config(text=f"Time: {self.time_left}")

        self.root.after(1000, self.update_timer)

    # ------------------------------------------------------------
    # End Game
    # ------------------------------------------------------------
    def end_game(self):
        self.game_running = False
        self.game_frame.pack_forget()

        for w in self.end_frame.winfo_children():
            w.destroy()

        self.end_frame.pack(expand=True)
        tk.Label(self.end_frame, text="TIME'S UP!", font=("Arial", 28)).pack(pady=20)
        tk.Label(self.end_frame, text=f"Your Score: {self.score}", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.end_frame, text="Play Again", font=("Arial", 18),
                  command=self.start_game).pack(pady=10)
        tk.Button(self.end_frame, text="Quit", font=("Arial", 18),
                  command=self.root.quit).pack()


# Run Game
root = tk.Tk()
app = CatchBallGame(root)
root.mainloop()