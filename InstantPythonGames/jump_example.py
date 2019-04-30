#company name
#game name
#team members
#two sentence explanation of the game's objective

from gamelib import*#import game library

#game object
game = Game (800,600,"Jumping Smurf")

#background object
bk = Image("bk.jpg",game)
bk.resizeTo(game.width, game.height)

game.setBackground(bk)

#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping
#smurf object
smurf = Animation("smurf_sprite.png",16,game,512/4,512/4)
smurf.moveTo(100,400)
smurf.stop()
#Level One game loop

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    smurf.draw()
    if smurf.y< 400:
        landed = False#not landed

    else:
        landed = True
   
            
    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
        #smurf.nextFrame()
        smurf.y -=27*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed: #is jumping
        smurf.y +=6#adjust for the height of the jump - lower number higher jump
        #smurf.nextFrame()




    if keys.Pressed[K_RIGHT]:
        smurf.nextFrame()#starts the animation
        smurf.x+=2
    if keys.Pressed[K_LEFT]:
        smurf.nextFrame()
       
        smurf.x-=2
        
    game.displayScore()
    game.update(60)
game.quit()
