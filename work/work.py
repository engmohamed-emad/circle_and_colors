import pygame 
import time
import sys
import random
#import pygame.display

pygame.init()


#================== colors ==========================================
White = (255,255,255)   # R G B
Purple = (128, 0, 128)
Pink =  (231, 84, 128)
Red= (255, 0, 0)
Green= (0, 255, 0)
Blue= (0, 0, 255)
Yellow= (255, 255, 0)
Cyan =(0, 255, 255)
Magenta= (255, 0, 255)
Orange= (255, 165, 0)
Purple= (128, 0, 128)
Pink= (255, 192, 203)
Brown= (165, 42, 42)
Gray= (128, 128, 128)
Light_Blue= (173, 216, 230)
Lime= (0, 255, 0)
Indigo= (75, 0, 130)
Violet= (238, 130, 238)
Teal= (0, 128, 128)
Navy= (0, 0, 128)
Olive= (128, 128, 0)
Gold= (255, 215, 0)
Maroon= (128, 0, 0)
Black=(0,0,0)

colors=[Red,Green,Blue,Yellow,Cyan,Magenta,Orange,Purple,Pink,Brown,Gray,Light_Blue,Lime,Indigo,Violet,Teal,Navy,
Olive,Gold,Maroon,White,Pink,Purple,Black]
#========================background==================================
window_width = 1100  # n 
window_height = 600  # m   
screen = pygame.display.set_mode((window_width,window_height))
rect_height=25
rect_width=25
rect_color=Green
rect_x=400
rect_y=400
circle_color=Yellow
circle_x=150
circle_y=150
circle_radius=50
pygame.draw.circle(screen,circle_color,(circle_x,circle_y),circle_radius)
flag=True
speed=2
background_color=(150,150,150)
#=====================================================================================================================

while True:  
  
 
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
        circle_x-=speed
        #circle_radius=0
  if keys[pygame.K_RIGHT]:
        circle_x+=speed
  if keys[pygame.K_UP]:
        circle_y-=speed
  if keys[pygame.K_DOWN]:
        circle_y+=speed
  if keys[pygame.K_b]:
        circle_radius+=.2
        if circle_radius>=150:
            circle_radius=150
  if keys[pygame.K_s]:
        circle_radius-=.2
        if circle_radius<=10:
            circle_radius=10
  if keys[pygame.K_EQUALS]:
      speed+=.01
      if speed>=10:
          speed=10
  if keys[pygame.K_MINUS]:
      speed-=.01
      if speed<=.5:
          speed=.5
   #=========================== to make circle free =====================================================================

  if circle_x>circle_radius+window_width:
      circle_x=-1*circle_radius
  if circle_x<-1*circle_radius:
      circle_x=circle_radius+window_width

  if circle_y>circle_radius+window_height:
      circle_y=-1*circle_radius
  if circle_y<-1*circle_radius:
      circle_y=circle_radius+window_height
  #=====================================================================================================================
  #================================   to make circle stuck =============================================================
  # if circle_x>=window_width-circle_radius:
  #     circle_x=window_width-circle_radius
  # if circle_x<=circle_radius:
  #     circle_x=circle_radius

  # if circle_y>=window_height-circle_radius:
  #     circle_y=window_height-circle_radius
  # if circle_y<=circle_radius:
  #     circle_y=circle_radius
  #=====================================================================================================================
 
  #========================================first game========================================================================
  in_x=(rect_x>=circle_x-circle_radius  and rect_x<=circle_x+circle_radius)
  in_y=(rect_y>=circle_y-circle_radius  and rect_y<=circle_y+circle_radius)
  
  if   in_x and in_y and flag:
      circle_color=rect_color
      flag=False
  #======================================================================================================================
  
  
  screen.fill(background_color)
  if flag:
      pygame.draw.rect(screen,rect_color,(rect_x,rect_y,rect_width,rect_height))
  pygame.draw.circle(screen,circle_color,(circle_x,circle_y),circle_radius)
  if not flag:
   rect_x=random.randint(0,window_width-rect_width)
   while rect_x>=circle_x-circle_radius and rect_x<=circle_x+circle_radius:
       rect_x=random.randint(0,window_width-rect_width)
   rect_y=random.randint(0,window_height-rect_height)
   while rect_y>=circle_y-circle_radius and rect_y<=circle_y+circle_radius:
       rect_y=random.randint(0,window_height-rect_height)
   idx=random.randint(0,len(colors)-1)
   rect_color=colors[idx]
   while rect_color== circle_color:
     idx=random.randint(0,len(colors)-1)
     rect_color=colors[idx]
   pygame.draw.rect(screen,rect_color,(rect_x,rect_y,rect_width,rect_height))
   flag=True
  pygame.display.update()
 
  pygame.time.Clock().tick(500)
  
 

  




#====================================================================

















