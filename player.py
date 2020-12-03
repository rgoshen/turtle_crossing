from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Class for turtle appearance and behavior."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()       
        self.setheading(90)
        
    def move_up(self):
        """Method to move player up the defined MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)
        
    def go_to_start(self):
        """Method to move player back to start."""
        self.goto(STARTING_POSITION)
        
    def is_at_finish_line(self):
        """Method returns true when player reaches finish line otherwise returns false."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
