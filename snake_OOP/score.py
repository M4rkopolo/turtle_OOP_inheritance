from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("hi score.txt", mode="r") as file: #reading the best score
            self.hi_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.add_points()


    def add_points(self):
        self.clear()
        self.write(f"score: {self.score}. hi score: {self.hi_score}", align="center", font=('Aria', 24, 'normal'))

    def game_over(self):                                    #change score to GAME OVER sentence
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Aria', 24, 'normal'))

    def reset(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open("hi score.txt", mode="w") as file:    #saving the best result if the old one is worse
                 file.write(f"{self.hi_score}")
        self.score = 0                                      #reseting current score
        self.add_points()


    def increase_score(self):
        self.score += 1
        self.add_points()