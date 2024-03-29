import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dis_width=800
dis_height=600
display=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Просто змейка')
clock=pygame.time.Clock()
snake_block=10
snake_speed=10
font_style=pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)
# sound=pygame.mixer.Sound('./musics/snake.mp3')
# sound.play()
def Your_score(score):
   value = score_font.render("Ваш счёт: " + str(score), True, yellow)
   display.blit(value, [0, 0])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display,black,[x[0],x[1],snake_block,snake_block])

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    display.blit(mesg,[dis_width/6,dis_height/3])

def game_loop():
    game_over=False
    game_close=False
    x1=dis_width/2
    y1=dis_height/2
    x1_change=0
    y1_change=0
    snake_List=[]
    length_of_snake=1
    foodx = round(random.randrange(1, dis_width-snake_block)/10.0)*10.0
    foody = round(random.randrange(1, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:
        while game_close==True:
            display.fill(yellow)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры!", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    elif event.key==pygame.K_c:
                        game_loop()    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True
        
        x1+=x1_change
        y1+=y1_change
        display.fill((100,200,100))
        pygame.draw.rect(display, white, [foodx, foody, snake_block, snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]  :
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_List)          
        #pygame.draw.rect(display,black,[x1,y1,10,10])
        Your_score(length_of_snake - 1)
        pygame.display.update()
        if x1==foodx and y1==foody:
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           length_of_snake += 1
        clock.tick(snake_speed)
        #pygame.display.update()      
    #time.sleep(3) 
    pygame.quit()
    quit()
game_loop()   