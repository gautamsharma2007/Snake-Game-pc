import sys
import random
import pygame
import time
from pygame.locals import *
pygame.init()
black=(0,0,0)
snklist=[]
GAME_SOUND={}
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
GAME_SOUND['point']=pygame.mixer.Sound('point.wav')
GAME_SOUND['die']=pygame.mixer.Sound('die.wav')
green=(0,255,0)
snakex=67
snakey=54
sizey=10
sizex=10
def plotsnake(screen,color,listc):
    for x,y in listc:

        pygame.draw.rect(screen,black,[x,y,sizex,sizey])
score=0
snklen=0
snakevelx=4
snakevely=0
font=pygame.font.SysFont(None,45)
def displayscore(score):
    score=font.render(text,True,blue)
    screen.blit(score,[10,10])
def displayover(s):
    s=font.render(text,True,red)
    screen.blit(s,[screenwidth/2,screenheight/2])
def iscollide(sx,sy,slist):
        for qx,qy in slist:
        #print(qx,qy)
            if abs(sx-qx)<10 and abs(sy-qy)<10:
                return

game_over=False
fps=32
clock=pygame.time.Clock()
screenheight=300
screenwidth=550
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Snakes game by Gautam Sharma")
foodx=random.randint(0,screenwidth)
foody=random.randint(0,screenheight)

while not game_over:
    screen.fill(white)
    pygame.draw.rect(screen,red,(foodx,foody,sizex,sizey))
    pygame.draw.rect(screen,black,(snakex,snakey,sizex,sizey))
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN and event.key==K_UP:
            snakevely=-4
            snakevelx=0
        if event.type==KEYDOWN and event.key==K_DOWN:
            snakevely=4
            snakevelx=0
        if event.type==KEYDOWN and event.key==K_RIGHT:
            snakevelx=4
            snakevely=0
        if event.type==KEYDOWN and event.key==K_LEFT:
            snakevelx=-4
            snakevely=0
    head=[]
    head.append(snakex)
    head.append(snakey)
    snklist.append(head)
    v=str(snklist)
    #print(snklist)
    plotsnake(screen,black,snklist)
    if snklen==0:
        snklen=len(snklist)
    if snklen<len(snklist):
        snklist.pop(0)
    snakex+=snakevelx
    snakey+=snakevely
    if abs(snakex-foodx)<8 and abs(snakey-foody)<8:
        score+=1
        GAME_SOUND['point'].play()
        snklen+=5
        foodx=random.randint(0,screenwidth-5)
        foody=random.randint(0,screenheight-5)
        f=open("highscore.txt","r")
        hiscore=f.read()
        f.close()
        k=int(hiscore)
        if score>k:
            k=open("highscore.txt","w")
            b=str(score)
            k.write(b)
            k.close()
    f=open("highscore.txt","r")
    hiscore=f.read()
    f.close()
    text="Score:"+str(score)+"      High score:"+hiscore
    displayscore(text)
    iscollide(snakex,snakey,snklist)
    if snakey<0 or snakey+10>screenheight or snakex<0 or snakex+10>screenwidth:
        
        print ("Game Over")
        screen.fill(white)
        z=open("highscore.txt","r")
        hiscore=z.read()
        displayover(f"game over ")
        GAME_SOUND['die'].play()
        pygame.display.update()
        time.sleep(1)
        z.close()
        game_over=True
    if head in snklist[:-1]:
        print ("Game Over")
        screen.fill(white)
        p=open("highscore.txt","r")
        hiscore=p.read()
        displayover(f"game over") 
        GAME_SOUND['die'].play()
        pygame.display.update()
        time.sleep(1)
        p.close()
        game_over=True    

        
    pygame.display.update()
    clock.tick(fps)