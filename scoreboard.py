from turtle import Turtle
# Constants for scoreboard alignment and font style
ALIGN = "center"
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the Scoreboard object."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        """Update the displayed score."""
        self.write(f"Score: {self.score} ", align= ALIGN, font=FONT)

    def game_over(self):
        """Display 'Game Over!' message."""
        self.goto(0,0)
        self.write("Game Over!", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increase the score and update the display."""
        self.score += 1
        self.clear()
        self.update_score()
