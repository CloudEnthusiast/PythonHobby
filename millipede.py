from turtle import Turtle, Screen
import random

SIZE = 20


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawself(self, turtle):
        """ draw a black box at its coordinates, with a small gap between cubes """

        turtle.goto(self.x - SIZE // 2 - 1, self.y - SIZE // 2 - 1)

        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(SIZE - SIZE // 10)
            turtle.left(90)
        turtle.end_fill()

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_blinking = True

    def changelocation(self):
        # it wont spawn outside the snake's body
        self.x = random.randint(0, SIZE) * SIZE - 200
        self.y = random.randint(0, SIZE) * SIZE - 200

    def drawself(self, turtle):
        # similar to the Square drawself, but will blink on / off
        if self.is_blinking:
            turtle.goto(self.x - SIZE // 2 - 1, self.y - SIZE // 2 - 1)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(SIZE - SIZE // 10)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        # logic to control the blinking
        self.is_blinking = not self.is_blinking

class Millipede:
    def __init__(self):
        self.headposition = [SIZE, 0]  # keeps track of traversing path while going
        self.body = [Square(-SIZE, 0), Square(0, 0), Square(SIZE, 0)]  # body will be a list of squares
        self.nextX = 1  # tells the snake which way it's going next
        self.nextY = 0
        self.crashed = False  # to detect collision
        self.nextposition = [self.headposition[0] + SIZE * self.nextX, self.headposition[1] + SIZE * self.nextY]
        # prepares the next location to add to the snake

    def moveOneStep(self):
        if Square(self.nextposition[0], self.nextposition[1]) not in self.body:
            # attempt (unsuccessful) at collision detection
            self.body.append(Square(self.nextposition[0], self.nextposition[1]))
            # moves the snake head to the next spot, deleting the tail
            del self.body[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
            # resets the head and nextposition
            self.nextposition = [self.headposition[0] + SIZE * self.nextX, self.headposition[1] + SIZE * self.nextY]
        else:
            self.crashed = True  # more unsuccessful collision detection

    def moveup(self):  # pretty obvious what these do
        self.nextX, self.nextY = 0, 1

    def moveleft(self):
        self.nextX, self.nextY = -1, 0

    def moveright(self):
        self.nextX, self.nextY = 1, 0

    def movedown(self):
        self.nextX, self.nextY = 0, -1

    def eatFood(self):
        # adds the next spot without deleting the tail, extending the snake by 1
        self.body.append(Square(self.nextposition[0], self.nextposition[1]))
        self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        self.nextposition = [self.headposition[0] + SIZE * self.nextX, self.headposition[1] + SIZE * self.nextY]

    def drawself(self, turtle):  # draws the whole millipede when called
        for segment in self.body:
            segment.drawself(turtle)

class Game:
    def __init__(self):
        # game object has a screen, a turtle, a basic millipede and a food
        self.screen = Screen()
        self.artist = Turtle(visible=False)
        self.artist.up()
        self.artist.speed("slowest")

        self.mp = Millipede()
        self.food = Food(100, 0)
        self.counter = 0  # this will be used later
        self.commandpending = False  # as will this

        self.screen.tracer(0)  # follow it so far?

        self.screen.listen()
        self.screen.onkey(self.mpdown, "Down")
        self.screen.onkey(self.mpup, "Up")
        self.screen.onkey(self.mpleft, "Left")
        self.screen.onkey(self.mpright, "Right")

    def nextFrame(self):
        self.artist.clear()

        if (self.mp.nextposition[0], self.mp.nextposition[1]) == (self.food.x, self.food.y):
            self.mp.eatFood()
            self.food.changelocation()
        else:
            self.mp.moveOneStep()

        if self.counter == 10:
            self.food.changestate()  # makes the food flash slowly
            self.counter = 0
        else:
            self.counter += 1

        self.food.drawself(self.artist)  # show the food and snake
        self.mp.drawself(self.artist)
        self.screen.update()
        self.screen.ontimer(lambda: self.nextFrame(), 100)

    def mpup(self):
        if not self.commandpending:
            self.commandpending = True
            self.mp.moveup()
            self.commandpending = False

    def mpdown(self):
        if not self.commandpending:
            self.commandpending = True
            self.mp.movedown()
            self.commandpending = False

    def mpleft(self):
        if not self.commandpending:
            self.commandpending = True
            self.mp.moveleft()
            self.commandpending = False

    def mpright(self):
        if not self.commandpending:
            self.commandpending = True
            self.mp.moveright()
            self.commandpending = False

game = Game()

screen = Screen()

screen.ontimer(lambda: game.nextFrame(), 100)
screen.mainloop()