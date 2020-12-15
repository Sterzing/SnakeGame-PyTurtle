from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.post_score()

    def post_score(self):
        self.goto(0, 275)
        self.write(f"Score: {self.score}", True, "center", ("Ariel", 20, "normal"))

    def award_point(self):
        self.clear()
        self.score += 1
        self.post_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, "center", ("Ariel", 20, "normal"))


