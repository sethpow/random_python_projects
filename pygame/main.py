import pygame
pygame.init()

win = pygame.display.set_mode((1500, 900))

pygame.display.set_caption("Castle Wars")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

# bulletSound = pygame.mixer.Sound('shoot.wav')
# hitSound = pygame.mixer.Sound('grunt.wav')
# bulletSound.play()
# hitSound.play()

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

score = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
            else:
                    win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) # (from line 29) makes the hitbox follow char. If it wasnt here, the box would stay at spawn
        # pygame.draw.rect(win, (150,0,0), self.hitbox,2) # char hitbox and color

# this makes char face the way he was moving, rather than looking forward once you stop moving side to side. 0 stays on first image


# this is for the bullet animation. Facing is telling which direction the bullet is travelling
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing
    
    # shape of the projectile
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y,), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]

    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5.75 # enemy speed
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 9
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 2 >= 33:
                self.walkCount = 0
        
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (185,30,30), (self.hitbox[0], self.hitbox[1] -20, 33.75, 10))
            pygame.draw.rect(win, (50, 145, 90), (self.hitbox[0], self.hitbox[1] -20, 40 - (3.75 * (10 - self.health)), 10)) #from 40/10 on, makes red appear when hit
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (250,0,0), self.hitbox,2)      # remove to make enemy hitbox appear
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print ('hit')


def redrawGameWindow():
    win.blit(bg, (0,0)) # this blocks the square from leaving a trail
    text = font.render('Player Score: ' + str(score), 1, (185,30,30))
    win.blit(text, (1215, 30)) # this draws the score text
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)   
    pygame.display.update()

# all pygames have main loop, for ex. collision, mouse events, hit stuff

# mainloop
font = pygame.font.SysFont('comicsans', 50) # font type, size, and bold
man = player(1245, 815, 64, 64) # char spawn point and size
goblin = enemy(200, 821, 64, 64, 1450) # enemy spawn and 1450 is where he turns back
bulletSpace = 0 # adding distance between bullets
bullets = []
run = True
while run:
    clock.tick(27)

    if bulletSpace > 0:
        bulletSpace += 1
    if bulletSpace > 3:
        bulletSpace = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: #checking to see if we are above bottom of rectangle, and checks if below top of rec
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                # hitSound.play()
                goblin.hit()
                score +=1
                bullets.pop(bullets.index(bullet)) # makes bullet dissappear on impact w/ goblin

        if bullet.x < 1500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            # makes the bullet dissappear


# movement and barriers
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bulletSpace == 0:
        # bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 3: # number of bullets our char can throw
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2), 6, (185,30,30), facing)) #bullet color
        bulletSpace = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1440 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    
    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
            
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    
    redrawGameWindow()

pygame.quit()
