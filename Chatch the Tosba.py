import turtle
from random import randint

#ekran ozellikleri
game_screen = turtle.Screen()
game_screen.bgcolor("beige")
game_screen.title("Catch the Tosba")

#tosbanın ozellikleri
tosba = turtle.Turtle()
tosba.color("beige")
tosba.hideturtle()
tosba.shape("turtle")
tosba.color("hot pink")
tosba.pensize(5)
tosba.speed(1)
tosba.penup()

#font
FONT = ('Arial', 15, 'bold')

#countdown icin turtle
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.color("plum")

#countdown fonksiyonu

def countdown(time):
    game_screen.onclick(None)
    text.clear()
    text.penup()
    text.goto(0, 220)
    text.pendown()

    if time > 0:
        tosba.showturtle()
        text.write(f"Time: {time}", align='center', font=FONT)
        game_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        tosba.hideturtle()
        text.penup()
        text.goto(0, 0)
        text.pendown()
        text.write("Game Over", align='center', font=FONT)

#score

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.color("plum")
score.goto(0, 250)
points = 0
def pointis():
    global points
    score.clear()
    points += 1
    score.write(f"Score: {points}", align='center', font=FONT)

tosba.onclick(lambda a,b : pointis())


#ready set go

text.write("Click for Start", align='center', font=FONT)
game_screen.onclick(lambda x, y: countdown(40))

#tosba hareket

while True:
    tosba.goto(randint(-200, 200), randint(-200, 200))
#buradan dolayı en son "Process finished with exit code 1" yazıyor.


turtle.mainloop()

"""
kaynaklar:
counter: https://stackoverflow.com/questions/63263036/displaying-timer-on-turtle-game
https://docs.python.org/3.11/library/turtle.html
"""