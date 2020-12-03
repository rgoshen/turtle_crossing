from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Class for scoreboard appearance and behavior."""
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        """Method to update the scoreboard."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        """Method to increase showed level."""
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        """Method to display game over."""
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
