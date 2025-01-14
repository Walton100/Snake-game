from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        with open('high_score',mode='r') as file:
            self.highscore=int(file.read())
        self.color('white')
        self.goto(-220, 250)
        self.write(f'SCORE:{self.score}', font=('Arial', 15, 'normal'))
        self.goto(0, 250)
        self.write(f'HIGHSCORE:{self.highscore}', font=('Arial', 15, 'normal'))


    def game_over(self):
        self.goto(-50,0)
        self.write(f'GAMEOVER', font=('Arial', 15, 'normal'))




    def update_score(self):



        self.goto(-220, 250)

        self.write(f'SCORE:{self.score}', font=('Arial', 15, 'normal'))



    def update_highscore(self):
        self.goto(0, 250)
        self.write(f'HIGHSCORE:{self.highscore}', font=('Arial', 15, 'normal'))








