from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player = 0
        self.r_player = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_player,align= "center",font = ("coirier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_player,align= "center",font = ("coirier", 80, "normal"))

    def l_point(self):
        self.l_player += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_player += 1
        self.update_scoreboard()