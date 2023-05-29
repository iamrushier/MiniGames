# Created by Vishwaved Kelkar
import pygame
from pygame.locals import *
import random  # Library to get random numbers and all

pygame.init()

clock = pygame.time.Clock()
fps = 60 # frames per seconnd are 60

screen_width = 494  # 318 ,864 ,289
screen_height = 782  # 936 ,511

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')  # To display the caption

# define font
font = pygame.font.SysFont('Bauhaus 93', 60)

# define colors
marroon = ((115, 0, 0))

# define game variables
ground_scroll = 0
scroll_speed = 4  # every iteration moves by 4 pixels
flying = False  # reference to 69,196,202,232,233
game_over = False
pipe_gap = 170
pipe_frequency = 1500  # milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# load images
bg = pygame.image.load('Gallery/Sprites/bg.png')
ground_img = pygame.image.load('Gallery/Sprites/Extra/ground1.png.png')
button_img = pygame.image.load('Gallery/Sprites/restart (1).png')


def draw_text(text, font, text_col, x, y):  # A fn for score of the user
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score


class Bird(pygame.sprite.Sprite):  # Here we are using sprite class
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #Sprite class has inbuilt draw,update functions that can be inherited
        self.images = []
        self.index = 0          # index is of the 'images' list which has 3 birds
        self.counter = 0  # it will control the speed of animation which is swapping from bird1 to bird2 to bird3
        for num in range(1, 4):  # range b/w 1-4 i.e. 3 as we've 3 images
            img = pygame.image.load(f'Gallery/Sprites/bird{num}.png')  # f stands for format of the string as we want
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]  # rect is used to create a rectangle at x and y coordinate
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying == True:
            # Gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            #print(self.vel)
            if self.rect.bottom < 670:
                self.rect.y += int(self.vel)

        if game_over == False:
            # To jump on clickimg the mouse
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # this in-built fn returns a list , 1 for mouse button has been clicked and here mouse is not clicked yet
                self.clicked = True
                self.vel = -10  # here we have taken vel as -ve bcoz +ve vel makes the bird to go down.

            if pygame.mouse.get_pressed()[0] == 0:  # this in-built fn returns a list , 0 for mouse button has been relleased
                self.clicked = False
                # self.vel = -10

            # Handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):  #  if this (self.index >= len(self.images) ) condition wouldnt be written then birds will change so fast from bird1-to-bird3
                    self.index = 0
            self.image = self.images[self.index]

            # To rotate the bird when it is moving up or down
            self.image = pygame.transform.rotate(self.images[self.index],-2.5 * self.vel)  # self.vel is +ve and due to it , it is moving in opposite sense so we have multiplied it by -ve number

        else:
            self.image = pygame.transform.rotate(self.images[self.index], -70)  # Bird rotates 70deg clockwise


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self) #inheriting sprite functions from Sprite class
        self.image = pygame.image.load('Gallery/Sprites/pipe (1).png')
        self.rect = self.image.get_rect()  # Creates rectangle boundary around it
        # position 1 is from the top and -1 from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True) #false for x axis , true for y axis ; as  we are flipping the y axis of the pipe
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:  # To erase the gone pipes , when a pipe crosses the 0 screenwidth it gets erased from the memory
            self.kill()


class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # Check if mouse is over the button "restart"
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:  # it returns 3 arguments - leftmost,middlemost and rightmost button,so here 0 means leftmost is clicked
                action = True

        # Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

# instances

flappy = Bird(50, int(screen_height / 2))  # Instance of Bird class , which is actual bird shown in the game

bird_group.add(flappy)  # add as same as append in this case

# creating restart button instance
button = button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

run = True  # until run is true  game will continue to un , the moment is gets false ; game will stop
while run:

    clock.tick(fps)

    screen.blit(bg, (0, 0))  # (0,0) indicates background image is blitted from left top corner ;blit is used to show the image
    # bg_scroll -= scroll_speed

    bird_group.draw(screen)  # draw is an built-in function in pygame - which actually draws the bird
    bird_group.update()

    pipe_group.draw(screen)  # draw is an built-in function in pygame - which actually draws the pipe

    # draw the ground
    screen.blit(ground_img, (ground_scroll, 670))  # Here x co-ordinate is 0 and y is height of the background image

    # Check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score), font, marroon, int(screen_width / 2), 20)

    # Check if bird has hit the ground
    if flappy.rect.bottom >= 670:  # flappy is the instance of the bird
        game_over = True
        flying = False

    # Check for collision with the pipe
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    if game_over == False and flying == True:

        # Generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-150, 150)  # 2 parameters to randint fn is the range the numbers would be generated from
            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height,-1)  # btm_pipe is the name of the instance of the Pipe
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        # Draw and scroll the ground
        ground_scroll -= scroll_speed  # ground_scroll is decreased by scroll_speed which results the ground to move into left side
        if abs(ground_scroll) > 25:  # It shifts the ground image , after every 25 pixels , to the left
            ground_scroll = 0

        pipe_group.update()

    # Check for game_over and reset
    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user presses the cross button , program will quit
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update() # updates everything thats has happened

pygame.quit()