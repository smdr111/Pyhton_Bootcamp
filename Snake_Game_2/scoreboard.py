from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier',24,'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file1:
           self.highscore = int(file1.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f'Score:{self.score}  High Score:{self.highscore}', align=ALIGNMENT,font=FONT)

    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt',mode='w') as file2:
                file2.write(f'{self.score}')
        self.score = 0
        self.update_board()

    def increase_score(self):
        self.score += 1
        self.update_board()


