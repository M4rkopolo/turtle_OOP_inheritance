import random
from turtle import Turtle, Screen

screen = Screen()
height = 600
width = 600
screen.setup(width=width, height=height)

# creating an instances of the Turtle class
tim = Turtle()
tom = Turtle()
zak = Turtle()
ala = Turtle()
wafel = Turtle()
mariusz = Turtle()
drawer = Turtle()
players = [tom, tim, mariusz, wafel, ala, zak]
names = ["tom", "tim", "mariusz", "wafel", "ala", "zak"]
colors = ["blue", "red", "yellow", "black", "pink", "grey", "orange", "brown", "green"]
the_end = False

def do_you_win(win, answer):
    winner = names[players.index(win)]
    if winner == answer.lower():
        next = screen.textinput("You win", f"BRAVO, You and {winner} wins.\n Do you want to play again? (Yes/No): ")
    else:
        next = screen.textinput("You lose", f"You and {answer} lose, The winner is {winner}.\n Do you want to play again? (Yes/No): ")
    if next.lower() == "yes":
        return False
    else:
        return True


def start():
    for player in players:
        player.shape("turtle")
        player.color(colors[players.index(player)])
        player.penup()
        player.setposition(-200, players.index(player)*20-50)


def window_on_screen(finish):
    winner = ""
    while not finish:
        for player in players:
            player.forward(random.randint(5, 20))
            actual_position = list(player.position())
            if actual_position[0] > 200:
                winner = player
                finish = True
    return winner

def draw_a_map():
    drawer.speed(9)
    drawer.penup()
    drawer.forward(200)
    drawer.setheading(90)
    drawer.forward(100)
    drawer.setheading(270)
    drawer.pendown()
    drawer.forward(250)
    drawer.penup()
    drawer.forward(400)


while not the_end:
    game = False
    screen.resetscreen()
    answer = screen.textinput("Title", "Who will win?\n Tin, Tom, Zak, Ala, Wafel czy Mariusz")
    draw_a_map()
    start()
    the_end = do_you_win(window_on_screen(game), answer)
screen.bye()
screen.exitonclick()