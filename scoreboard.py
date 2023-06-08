from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            my_score = int(file.read())
        self.high_score = my_score
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(-80, 275)
        self.write(f"Score {self.score}", align="center", font=("Arial", 13, "bold"))
        self.goto(80, 275)
        self.write(f"High Score {self.high_score}", align="center", font=("Arial", 13, "bold"))

    def score_update(self, x):
        if x == 0:
            self.score += 1
        self.clear()
        self.goto(-80, 275)
        self.write(f"Score {self.score}", align="center", font=("Arial", 13, "bold"))
        self.goto(80, 275)
        self.write(f"High Score {self.high_score}", align="center", font=("Arial", 13, "bold"))

    def check_highest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                my_score = int(file.write(str(self.score)))

    def reset_score(self):
        self.check_highest_score()
        self.score = 0
        self.score_update(1)
