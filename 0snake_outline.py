from microbit import *
from random import randint

def random_point():
    """ This function returns a random point
        on the playing board
    """
    return [randint(0, 4), randint(0, 4)]


class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
    """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
                game = Snake()
            init stands for "Initialisation"
        """
        ## UNCOMMENT AND FILL IN THE # LINES BELOW WITH START VALUES
        ## current direction is a string with up, down, left or right
        self.current_direction = "up"
        ## snake is a list of the pixels that the snake is at
        self.snake = [[2, 2]]
        ## food is the co-ords of the current food
        self.food = random_point()
        ## whether or not to end the game, used after update
        self.end = False
        pass

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
        """
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        # abs is the absolute function eg -1 => 1, 1 => 1
        if abs(x) > abs(y):
            if x < 0:
                self.current_direction = "left"
            else:
                self.current_direction = "right"
        else:
            if y < 0:
                self.current_direction = "up"
            else:
                self.current_direction = "down"

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        # The line below makes a copy of the head of the snake
        # you will be working with that copy in this function
        new_head = list(self.snake[-1])


    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        if self.food[0] >= 0 and self.food[0] <= 4 and self.food[1] >= 0 and self.food[1] <= 4:
            display.set_pixel(self.food[0], self.food[1], 5)
        for part in self.snake:
            if part[0] >= 0 and part[0] <= 4 and part[1] >= 0 and part[1] <= 4:
                display.set_pixel(part[0], part[1], 9)

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while not game.end:
    game.handle_input()
    game.update()
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)

display.show("Game over")
