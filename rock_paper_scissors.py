import turtle
from time import sleep
import random

#====Start Screen====
start = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('misty rose')
wn.tracer(False)
start.pencolor('crimson')
start.pu()
font = ('Arial', 40, 'bold')
start.write('Rock Paper Scissor', font=font, align='center')
start.color('green')
start.shape('triangle')
start.shapesize(4)
start.sety(-50)
wn.tracer(True)

#Shapes
object_pic = ['bot.gif', 'you.gif', 'rock.gif', 'paper.gif','scissor.gif', 'play_again.gif']
for shape in range(len(object_pic)):
        wn.addshape(object_pic[shape])
        
#Win Condition:
win_cond =  {'rock.gif': 'scissor.gif',
            'scissor.gif': 'paper.gif',
            'paper.gif': 'rock.gif'}

#====Selection====
def pick():
    global bot_shape
    bot_shape=random.choice(object_pic[2:5])
    global announce
    wn.tracer(False)
    announce = turtle.Turtle()
    announce.turtlesize(4)
    announce.pencolor('crimson')
    announce.shape('triangle')
    announce.hideturtle()
    announce.pu()
    wn.tracer(True)
    for shape in object_pic[2:5]:
        for fist in fist_object:
            fist.shape(shape)
        announce.write(shape.rstrip('.gif').title(), align='center', font=font)
        sleep(1)
        announce.clear()
    announce.write('Shoot', align='center', font=font)
    fist_object[0].shape(bot_shape)

def rock(x, y):
    pick()
    global player_shape
    player_shape = 'rock.gif'
    fist_object[1].shape(player_shape)
    check_winner()
    
def paper(x, y):
    pick()
    global player_shape
    player_shape = 'paper.gif'
    fist_object[1].shape(player_shape)
    check_winner()
    
def scissor(x, y):
    pick()
    global player_shape
    player_shape = 'scissor.gif'
    fist_object[1].shape(player_shape)
    check_winner()
    
def check_winner():
    sleep(1)
    if win_cond[player_shape] == bot_shape:
        declare_winner('You Wins!')
    elif win_cond[bot_shape] == player_shape:
        declare_winner('Bot Wins!')
    else:
        declare_winner("It's a Tie!")

def declare_winner(winner):
    announce.clear()
    announce.write(winner, align='center', font=font)
    announce.speed(0)
    announce.goto(-10, -50)
    announce.showturtle()
    announce.shape('play_again.gif')
    announce.onclick(game_screen)

#====Game====
def game_screen(x, y):
    wn.clear()
    wn.bgcolor('misty rose')
    font = ('Arial', 20, 'bold')
    wn.tracer(False)
    global fist_object
    fist_object = []
    fist_xcor = (300, -300)
    for num, fists in enumerate(object_pic[0:2]): #Create the two fist 
        fist = turtle.Turtle()
        fist.speed(0)
        fist.shape(fists)
        fist.pu()
        fist.pencolor('dark orange')
        fist.setx(fist_xcor[num])
        fist.sety(100)
        fist.write(fists.rstrip('.gif').title(), align='center', font=font)
        fist.sety(0)
        fist_object.append(fist)
    global player_choice
    player_choice = []
    choice_config = ((-200, rock), (0, paper), (200, scissor))
    for num, option in enumerate(range(2, 5)): #Create the clickable player_choice (Rock, Paper, or Scissor)
        choice = turtle.Turtle()
        choice.speed(0)
        choice.shape(object_pic[option])
        choice.pu()
        choice.goto(choice_config[num][0], -250)
        choice.onclick(choice_config[num][1])
        player_choice.append(choice)
    wn.tracer(True)
    
start.onclick(game_screen)
wn.mainloop()