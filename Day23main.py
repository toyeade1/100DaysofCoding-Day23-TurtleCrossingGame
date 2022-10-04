import time
from turtle import Screen
from Day23player import Player
from Day23car_manager import CarManager
from Day23scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(fun=player.move, key='Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

# Detect car for collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

# Detect if the turtle has successfully crossed.
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.add_level()
        scoreboard.update_scoreboard()




screen.exitonclick()


