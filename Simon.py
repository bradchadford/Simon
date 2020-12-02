import random
import time

# Class 1 Button:
# For the text version each button class stores its color and current location on the 2 by 2 colored grid
class Button:
    def __init__(self, clr, pos):
        self.value = clr
        self.position = pos

    def reposition(self, new_pos):
        self.position = new_pos

    def print_color_option(self):
        clr_dict = {'R': 'RED', 'G': 'GREEN', 'B': 'BLUE', 'Y': 'YELLOW'}
        return clr_dict[self.value]

    def __str__(self):
        return "{}: {}".format(self.position, self.print_color_option())

# Class 2 Simon:
# Main class
class Simon:
    def __init__(self):
        # Default grid setting
        green = Button('G', 'TL')
        red = Button('R', 'TR')
        blue = Button('B', 'BR')
        yellow = Button('Y', 'BL')
        # positions: top left, top right, bottom right, bottom left ( Used for adding parameters for the button class)
        self.positions = ['TL', 'TR', 'BR', 'BL']
        self.display_order = [green, red, blue, yellow]
        self.choices = ['G', 'R', 'B', 'Y', 'LT', 'RT', 'FL']
        self.sequence = []
        self.round = 0
    # Initializes game. Increments the round by 1 and adds another item to the sequence
    def play(self):
        self.sequence.append(random.choice(self.choices))
        self.round += 1
        for i in range(len(self.sequence)):
            if self.sequence[i] == 'RT':
                self.rotate_right()
            if self.sequence[i] == 'LT':
                self.rotate_left()
            if self.sequence[i] == 'FL':
                self.flip()

    def rotate_left(self):
        self.display_order.append(self.display_order.pop(0))
        for i in range(len(self.display_order)):
            self.display_order[i].reposition(self.positions[i])

    # Below I could have used d different append method but decided recycling rotate_left is more readable
    def rotate_right(self):
        for i in range(3):
            self.rotate_left()
    # Flip in a 3D environment would look like the flip of a coin thus inverting the colors 
    def flip(self):
        for i in range(2):
            self.rotate_left()

    def __str__(self):
        to_print = 'Round: ' + str(self.round) + '\n'
        for btn in self.display_order:
            to_print += str(btn) + ', '
        to_print = to_print[:-2]
        to_print += '\nSequence: '
        for i in self.sequence:
            to_print += str(i) + ', '
        to_print = to_print[:-2]
        return to_print


game = Simon()
print('Simon Says...')

game_status = 'Win'
while game_status == 'Win':
    game.play()
    print(game)
    response = input('Your turn complete the sequence (separated by spaces:\n').upper().split()

    if response == game.sequence:
        game_status = 'Win'
        print('Correct!')
    else:
        game_status = 'Lose'
        print('Incorrect... You Lose!')











