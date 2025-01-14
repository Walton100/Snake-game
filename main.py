from turtle import Turtle,Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)
food=Food()
snake=Snake()

scoreboard=ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up,key='w')
screen.onkey(fun=snake.down,key='s')
screen.onkey(fun=snake.left,key='a')
screen.onkey(fun=snake.right,key='d')



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.068)
    snake.move_snake()



    if food.distance(snake.segments[0]) < 20  :
        food.respawn()
        snake.grow()
        scoreboard.score+=1
        scoreboard.clear()
        scoreboard.update_score()
        scoreboard.update_highscore()



    if snake.hit_wall() or snake.hit_body():


        snake.respawn()



        if scoreboard.highscore<scoreboard.score:
            scoreboard.highscore=scoreboard.score
            scoreboard.update_highscore()
            scoreboard.score = 0
            scoreboard.clear()
            scoreboard.update_score()
            scoreboard.update_highscore()
        elif scoreboard.highscore>=scoreboard.score:
            with open('high_score',mode='w') as file:
                file.write(f'{scoreboard.highscore}')

            scoreboard.score = 0
            scoreboard.clear()
            scoreboard.update_score()
            scoreboard.update_highscore()



screen.exitonclick()



