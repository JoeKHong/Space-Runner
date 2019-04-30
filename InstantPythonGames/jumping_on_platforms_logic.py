from gamelib import*

#game object
game = Game (800,600,"AnimationGame")
#bk object
bk = Image("bk2.png",game)
bk3 = Image("bk3.jpg", game)
           
bk.resizeTo(game.width, game.height+20)
bk3.resizeTo(game.width, game.height)

game.setBackground(bk)

        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping
count = 0

#smurf object
smurf = Animation("smurf_sprite.png",16,game,512/4,512/4)
smurfL = Animation("smurf_spriteL.png",16,game,512/4,512/4)
smurf.moveTo(100,500)

smurfL.visible = False



tramp = Image("tramp.png",game)
tramp.resizeBy(-60)
tramp.y = 500
ontramp = False
#Jump and Land 

while not game.over:
    game.processInput()
    bk3.draw()
    tramp.draw()
    smurfL.moveTo(smurf.x,smurf.y)
    smurf.draw()
    smurfL.draw()
    if keys.Pressed[K_RIGHT]:
        smurf.visible = True
        smurfL.visible = False
        smurf.x+=3
        smurfL.x+=3
        
        
    if keys.Pressed[K_LEFT]:
        
        smurf.visible = False
        smurfL.visible = True
        smurf.x-=3
        smurfL.x-=3
        
    if keys.Pressed[K_UP]:
        smurf.y-=1
       
    if keys.Pressed[K_DOWN]:
       smurf.y+=1
        
    if smurf.y< 500 and not ontramp:# if object has not landed on ground 
        landed = False#not landed
     
    else:
        landed = True#landed

    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not already jumping and spacebar is pressed 
        jumping = True

    if jumping: #decision above tests to true
        smurf.y -=37*factor#higher value the higher the jump
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95
        landed = False
        ontramp = False#add this action if jumping 
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1

    if not landed:
        smurf.y +=8 #adjust as needed (lower number higher jump)

    if smurf.collidedWith(tramp,"rectangle")and smurf.x>tramp.left and smurf.x<tramp.right and smurf.y>tramp.top and smurf.y<tramp.y+50:
        ontramp = True

    if smurfL.collidedWith(tramp,"rectangle")and smurfL.x>tramp.left and smurfL.x<tramp.right and smurfL.y>tramp.top and smurfL.y<tramp.y+50:
        ontramp = True

    if ontramp and smurf.x>tramp.right and not jumping:#character has landed on ramp and moves off to the right and is not jumping (to start tbe jumping test again)
        ontramp = False
        smurf.y +=8 #adjust as needed (lower number higher jump)

    if ontramp and smurfL.x<tramp.left and not jumping:#character has landed on ramp and moves off to the left and is not jumping (to start tbe jumping test again)
        ontramp = False
        smurfL.y +=8 #adjust as needed (lower number higher jump)
        
    
        

    
    
    game.update(60)
game.over = False
game.quit()





