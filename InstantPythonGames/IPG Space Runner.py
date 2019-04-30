from gamelib import *
game = Game(1000, 800, "Space Runner")
bk = Image("Space REAL.png", game)
game.setBackground(bk)

runner = Image("Space Runner man.png", game)
enemy = Image("Space Runner Enemy 2.png", game)
coin = Image("Space Runner Coin.jpg", game)
ammo = Image("Space Runner Ammo.jpg", game)
asteroid = Image("asteroid2.png", game)
title = Image("Space Runner Title Screen.png", game)
play = Image("play button.png", game)
plasma = Image("plasma ball 2.gif", game)

y = randint(100, 700)

title.x = 500
title.y-=100

play.x = 500
play.y+= 250

runner.resizeBy(-70)
play.resizeBy(-30)

coin.setSpeed(5, 45)
ammo.setSpeed(5, 75)

plasma.setSpeed(50, 270)
plasma.resizeBy(-90)

coin.visible=True
ammo.visible=True

jumping = False
landed = False
factor = 1
count = 0
onasteroid = False

runner.health = 350
runner.ammo = 0

enemies = []
for index in range(10):
    enemies.append(Image("Space Runner Enemy 2.png", game))

for index in range(10):
    x = 1100
    y =randint (100, 700)
    enemies[index].resizeBy(-70)
    enemies[index].setSpeed(8, 90)
    
    
                  
asteroid = []
for index in range(10):
    asteroid.append(Image("asteroid2.png", game))
for index in range(10):
    x = 1100
    y = randint(100,700)
    #asteroid[index].moveTo(x, y)
    asteroid[index].x = x
    asteroid[index].y = y
    asteroid[index].setSpeed(6, 90)
    asteroid[index].resizeBy(-60)

#Title Screen
while not game.over:
    game.processInput()
    game.scrollBackground("left", 3)
    title.draw()
    play.draw()
    

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(60)


game.over = False

                  
#Level One
while not game.over:
    game.processInput()

    game.scrollBackground("left", 3)
    runner.draw()

    
       
    plasma.move(False)

    for index in range(10):
        asteroid[index].move(False)

    for index in range(randint(1, 5)):
        y = randint(100, 800)
        if asteroid[index].isOffScreen("left"):
            asteroid[index].moveTo(1100, y)
            print(y)
            asteroid[index].visible=True
    
    for index in range(10):
        enemies[index].move(False)
    for index in range(randint(1, 5)):
        y = randint(100, 800)
        if asteroid[index].isOffScreen("left"):
            asteroid[index].moveTo(1100, y)
            print(y)
                       
    if enemies[index].isOffScreen("left"):
        enemies[index].moveTo(1100,y)
        enemies[index].visible=True

    if runner.collidedWith(enemies[index]):
        runner.health-= 10

    if plasma.collidedWith(enemies[index]):
        enemies[index].visible=False

    if runner.health<10:
        game.over = True


    if runner.collidedWith(enemies[index]):
        enemies[index].visible=False

    game.drawText("Health :"+str(runner.health), runner.x, runner.y+20)
    
    
    #adding to players score?
    
    if runner.y< 400 and not onasteroid:
        landed = False

    else:
        landed = True
   
    if keys.Pressed[K_UP] and landed and not jumping:
        jumping = True

    if jumping:
        
        runner.y -=27*factor
        factor*=.95
        landed = False
        if factor < .18:
            jumping = False
            
            factor = 1
            
    if not landed: 
        runner.y +=6

    if keys.Pressed[K_RIGHT]:
        runner.x+=2
    if keys.Pressed[K_LEFT]:
        runner.x-=2

    for index in range(10): 
        if plasma.collidedWith(enemies[index]):
            game.score+=10



    game.displayScore()



    if keys.Pressed[K_DOWN]:

        runner.y+=10
    if keys.Pressed[K_LEFT]:
        runner.x-=10
    if keys.Pressed[K_RIGHT]:
        runner.x+=10

    if keys.Pressed[K_SPACE]:
        plasma.moveTo(runner.x+10, runner.y)
        

    if runner.collidedWith(asteroid[index]):
        runner.health-=5
        

    if runner.collidedWith(asteroid[index]):
        asteroid[index].visible=False

    if plasma.collidedWith(asteroid[index]):
        asteroid[index].visible=False
    game.update(60)

game.over = False

#End screens


game.quit()

