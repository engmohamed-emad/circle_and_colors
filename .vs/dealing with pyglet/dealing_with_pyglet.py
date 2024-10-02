from math import sqrt
from turtle import window_width
import pyglet
from pyglet.window import key
import os
import math


start_x=25
scale=1
speed_b=1000
speed_p=800
player_height=player_width=90
ball_width=ball_height=66
window_height=750
window_width=1280
moving=0
ball_dir="no"
score_r=0
score_b=0





window = pyglet.window.Window(width=window_width, height=window_height, caption="Air Hockey")


#===============blue player=========================================================================================================
player_red_image = pyglet.image.load("C:\\Users\\Mohamed Emad\\source\\repos\\dealing with pyglet\\my_images\\blue_player.png")
player_red = pyglet.sprite.Sprite(player_red_image, x=start_x, y=window_height/2-player_height/2)
player_red.scale=scale
player_red_dx = speed_p
player_red_dy = speed_p  
#===============blue player=========================================================================================================
player_blue_image = pyglet.image.load("C:\\Users\\Mohamed Emad\\source\\repos\\dealing with pyglet\\my_images\\red_player.png")
player_blue = pyglet.sprite.Sprite(player_blue_image, x=window_width-player_width-start_x, y=window_height/2-player_height/2)
player_blue.scale=scale
player_blue_dx = speed_p
player_blue_dy = speed_p
#===============ball ==================================================================================================================
ball_image=pyglet.image.load("C:\\Users\\Mohamed Emad\\source\\repos\dealing with pyglet\\my_images\\ball.png")
ball=pyglet.sprite.Sprite(ball_image,x=window_width/2-ball_width//2,y=window_height/2-ball_height//2)
ball.scale=scale
ball_dx = speed_b
ball_dy = speed_b

#=====================================================================================================================================
background = pyglet.image.load("C:\\Users\\Mohamed Emad\\source\\repos\\dealing with pyglet\\my_images\\court.png")
keys = key.KeyStateHandler()
window.push_handlers(keys)
#================================================================================================================================
goal_y_s=220
goal_y_e=530
#================================================================================================================================
def update(dt):
    global player_red_dx, player_red_dy, player_blue_dx, player_blue_dy,ball_dx,ball_dy,ball_dir,moving,speed_p,speed_b,score_b,score_r,start_x
    def center():
         ball.y=window.height//2-ball.height//2
         player_red.x=start_x
         player_red.y=window.height//2-player_height//2
         player_blue.x=window_width-player_width-start_x
         player_blue.y=window.height//2-player_height//2
    #==========for player red===============================================================================================================
     
    pr_center_x = player_red.x+player_red.width//2
    pr_center_y = player_red.y+player_red.height//2

    if keys[key.A]:
      player_red.x -= player_red_dx * dt
    elif keys[key.D]:
      player_red.x += player_red_dx * dt
    elif  keys[key.W]:
      player_red.y += player_red_dx * dt
    elif keys[key.S]:
      player_red.y -= player_red_dy * dt

    if player_red.x <= 0  or player_red.x + player_red.width >= window.width//2 :
        if player_red.x <= 0:
            player_red.x=0
        else :
            player_red.x = window.width//2- player_red.width

    if player_red.y <= 0 or player_red.y + player_red.height >= window.height:
       if player_red.y <= 0:
            player_red.y=0
       else :
            player_red.y=window.height-player_red.height

    #===============for player blue=========================================================================================================      
    pb_center_x = player_blue.x+player_blue.width//2
    pb_center_y = player_blue.y+player_blue.height//2

    if keys[key.LEFT]:
      player_blue.x -= player_blue_dx * dt
    elif keys[key.RIGHT]:
      player_blue.x += player_blue_dx * dt
    elif  keys[key.UP]:
      player_blue.y += player_blue_dx * dt
    elif keys[key.DOWN]:
      player_blue.y -= player_blue_dy * dt

    if player_blue.x <= window_width//2 or player_blue.x + player_blue.width >= window.width:
        if player_blue.x <= window_width//2:
            player_blue.x=window_width//2
        else :
            player_blue.x=window_width-player_blue.width

    if player_blue.y <= 0 or player_blue.y + player_blue.height >= window.height:
       if player_blue.y <= 0:
            player_blue.y=0
       else :
            player_blue.y=window.height-player_blue.height

    #=============== ball ==========================================================================================================================
    ball_center_y=ball.y+ball_height//2
    ball_center_x=ball.x+ball_width//2
    
    ball.x+=ball_dx*dt*moving
    ball.y+=ball_dy*dt*moving
    #==========================collsion=====================================================================
    roots=ball.height//2+player_height//2
    distance_r=(math.sqrt(pow(ball_center_x-pr_center_x,2)+pow(ball_center_y-pr_center_y,2)))
    distance_b=(math.sqrt(pow(ball_center_x-pb_center_x,2)+pow(ball_center_y-pb_center_y,2)))
    if roots>=distance_r or roots>=distance_b:
        moving=1
        if roots>=distance_r:
            dx=ball_center_x-pr_center_x
            dy=ball_center_y-pr_center_y
            ball_dx=(speed_b//(abs(dx)+abs(dy)))*dx 
            ball_dy=(speed_b//(abs(dx)+abs(dy)))*dy 
        else:
            dx=ball_center_x-pb_center_x
            dy=ball_center_y-pb_center_y
            ball_dx=(speed_b//(abs(dx)+abs(dy)))*dx 
            ball_dy=(speed_b//(abs(dx)+abs(dy)))*dy 


    #======================================================================================================

    if ball.x<=0 or ball.x+ball.width>=window.width:
        if ball.x<=0:
            if ball.y>=200 and ball.y+ball.height<=550:
                if ball.x<=-1*ball.width:
                    score_r+=1
                    center()
                    ball.x=window.width//2-ball.width-100
                    moving=0
                   
            else:
              ball.x=0
              ball_dx*=-1
              

        else :
            if ball.y>=200 and ball.y+ball.height<=550:
                if ball.x>=window.width+ball.width:
                    score_b+=1
                    center()
                    ball.x=window.width//2+100
                    moving=0
                    
            else:
              ball.x=window_width-ball.width
              ball_dx*=-1
       
        

    if ball.y<=0 or ball.y+ball.height>=window.height:
        if ball.y<=0:
          ball.y=0
        else :
          ball.y=window_height-ball.height
      
        ball_dy*=-1


   
    label_b = pyglet.text.Label(
    str(score_b),
    font_name='Arial',
    font_size=24,
    x=window.width//2-50,
    y=window.height-50,
    anchor_x='center',
    anchor_y='center',
    color=(0, 0,255, 255) 
    )
    label_r = pyglet.text.Label(
    str(score_r),
    font_name='Arial',
    font_size=24,
    x=window.width // 2+50,
    y=window.height-50,
    anchor_x='center',
    anchor_y='center',
    color=(255, 0, 0, 255) 
    )
    @window.event
    def on_draw():
        window.clear()
        background.blit(0, 0) 
        player_red.draw()
        player_blue.draw()
        ball.draw()
        label_r.draw()
        label_b.draw()
   # @window.event
    def on_mouse_motion(x, y, dx, dy):
     print(f'Mouse coordinates: ({x}, {y})')
#============================================================================================================================


pyglet.clock.schedule_interval(update, 1/1000.0)

pyglet.app.run()
