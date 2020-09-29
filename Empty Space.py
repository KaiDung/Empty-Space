import pygame
import random
import numpy as np
import cv2

pygame.init() #turn all of pygame on.
pygame.mixer.init()

black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

lower_blue = np.array([110, 50, 50], dtype=np.uint8)
upper_blue = np.array([130, 255, 255], dtype=np.uint8)
cap = cv2.VideoCapture(0)

display_width = 1024
display_height = 768

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Empty Space')
clock = pygame.time.Clock()

Background_music = pygame.mixer.music.load('./music/Dreaming_Blue.ogg')
pygame.mixer.music.play(-1)

laser_sound = pygame.mixer.Sound("./music/laser.wav")
laser_sound.set_volume(0.5)

# player準備
player1 = pygame.image.load('./pic/player.png')
player2 = pygame.image.load('./pic/newplayer.png')
Health4 = pygame.image.load('./pic/Health4.png')
Health3 = pygame.image.load('./pic/Health3.png')
Health2 = pygame.image.load('./pic/Health2.png')
Health1 = pygame.image.load('./pic/Health1.png')
# 子彈
bullet1 = pygame.image.load('./pic/bullet1.png')

bullet_img = pygame.image.load('./pic/bullet_img.png')
#道具
update_item = pygame.image.load('./pic/update_item.png')
health_item = pygame.image.load('./pic/health_item.png')
# 背景
background = pygame.image.load('./pic/background.jpg')
gameover = pygame.image.load('./pic/gameover.jpg')
win = pygame.image.load('./pic/win.jpg')
menu = pygame.image.load('./pic/menu.png')
# 火球
fireball1 = pygame.image.load('./pic/fireball1.png')
#Boss準備
Boss1 = pygame.image.load('./pic/Boss1.png')
Boss2 = pygame.image.load('./pic/Boss2.png')
Boss3 = pygame.image.load('./pic/Boss3.png')
Boss4 = pygame.image.load('./pic/Boss4.png')
BossHealth10_2 = pygame.image.load('./pic/BossHealth10_2.png')
BossHealth9_2 = pygame.image.load('./pic/BossHealth9_2.png')
BossHealth8_2 = pygame.image.load('./pic/BossHealth8_2.png')
BossHealth7_2 = pygame.image.load('./pic/BossHealth7_2.png')
BossHealth6_2 = pygame.image.load('./pic/BossHealth6_2.png')
BossHealth5_2 = pygame.image.load('./pic/BossHealth5_2.png')
BossHealth4_2 = pygame.image.load('./pic/BossHealth4_2.png')
BossHealth3_2 = pygame.image.load('./pic/BossHealth3_2.png')
BossHealth2_2 = pygame.image.load('./pic/BossHealth2_2.png')
BossHealth1_2 = pygame.image.load('./pic/BossHealth1_2.png')
BossHealth10 = pygame.image.load('./pic/BossHealth10.png')
BossHealth9 = pygame.image.load('./pic/BossHealth9.png')
BossHealth8 = pygame.image.load('./pic/BossHealth8.png')
BossHealth7 = pygame.image.load('./pic/BossHealth7.png')
BossHealth6 = pygame.image.load('./pic/BossHealth6.png')
BossHealth5 = pygame.image.load('./pic/BossHealth5.png')
BossHealth4 = pygame.image.load('./pic/BossHealth4.png')
BossHealth3 = pygame.image.load('./pic/BossHealth3.png')
BossHealth2 = pygame.image.load('./pic/BossHealth2.png')
BossHealth1 = pygame.image.load('./pic/BossHealth1.png')
BossHealth0 = pygame.image.load('./pic/BossHealth0.png')


class Bullet():
    def __init__(self,now_x,now_y):
        self.now_x = now_x
        self.now_y = now_y

class Fireball():
    def __init__(self,fb_x,fb_y):
        self.fb_x = fb_x
        self.fb_y = fb_y

#升級道具飛行
def GiveItem(item,x,y):
    gameDisplay.blit(item,(x,y))

#玩家顯示
def Player1Display(update,Health,x, y):
    if update==1:
        gameDisplay.blit(player2, (x, y))
    else:
        gameDisplay.blit(player1, (x, y))
    if Health == 4:
        gameDisplay.blit(Health4, (5,5 ))
    elif Health == 3:
        gameDisplay.blit(Health3, (5,5 ))
    elif Health == 2:
        gameDisplay.blit(Health2, (5,5 ))
    elif Health == 1:
        gameDisplay.blit(Health1, (5, 5))

#子彈數量顯示
def BulletDisplay(number_of_bullet):
    if number_of_bullet > 0:
        gameDisplay.blit(bullet_img,(25,60))
    if number_of_bullet > 1:
        gameDisplay.blit(bullet_img, (45, 60))
    if number_of_bullet > 2:
        gameDisplay.blit(bullet_img, (65, 60))
    if number_of_bullet > 3:
        gameDisplay.blit(bullet_img, (85, 60))

#Boss顯示
def BossDisplay(Boss_state,Boss_x,Boss_y):
    if Boss_state==1:
        gameDisplay.blit(Boss1,(Boss_x,Boss_y))
    if Boss_state==2:
        gameDisplay.blit(Boss2,(Boss_x,Boss_y))
    if Boss_state==3:
        gameDisplay.blit(Boss3,(Boss_x,Boss_y))
    if Boss_state==4:
        gameDisplay.blit(Boss4,(Boss_x,Boss_y))

#Boss血量顯示
def BossHealthDisplay(Boss_Health,x,y):
    if Boss_Health==20:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth10_2,(x,y))
    if Boss_Health==19:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth9_2,(x,y))
    if Boss_Health==18:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth8_2,(x,y))
    if Boss_Health==17:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth7_2,(x,y))
    if Boss_Health==16:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth6_2,(x,y))
    if Boss_Health==15:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth5_2,(x,y))
    if Boss_Health==14:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth4_2,(x,y))
    if Boss_Health==13:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth3_2,(x,y))
    if Boss_Health==12:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth2_2,(x,y))
    if Boss_Health==11:
        gameDisplay.blit(BossHealth10,(x,y))
        gameDisplay.blit(BossHealth1_2,(x,y))
    if Boss_Health==10:
        gameDisplay.blit(BossHealth10,(x,y))
    if Boss_Health==9:
        gameDisplay.blit(BossHealth9,(x,y))
    if Boss_Health==8:
        gameDisplay.blit(BossHealth8,(x,y))
    if Boss_Health==7:
        gameDisplay.blit(BossHealth7,(x,y))
    if Boss_Health==6:
        gameDisplay.blit(BossHealth6,(x,y))
    if Boss_Health==5:
        gameDisplay.blit(BossHealth5,(x,y))
    if Boss_Health==4:
        gameDisplay.blit(BossHealth4,(x,y))
    if Boss_Health==3:
        gameDisplay.blit(BossHealth3,(x,y))
    if Boss_Health==2:
        gameDisplay.blit(BossHealth2,(x,y))
    if Boss_Health==1:
        gameDisplay.blit(BossHealth1,(x,y))
    if Boss_Health<=0:
        gameDisplay.blit(BossHealth0,(x,y))

#Boss攻擊
def Boss_Attack(x,y):
    gameDisplay.blit(fireball1, (x, y))

#子彈飛行
def update_bullet(bullet1x,bullet1y):
    gameDisplay.blit(bullet1,(bullet1x,bullet1y))


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()

def GameOver():
    gameoverexit = False
    while not gameoverexit:
        gameDisplay.blit(gameover, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Try Again", 512 - 200 - 100, 650, 100, 50, green, bright_green, game_loop)
        button("Quit", 512 + 200, 650, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(100)

def Win():
    winexit = False
    while not winexit:
        gameDisplay.blit(win, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 512 - 200 - 100, 650, 100, 50, green, bright_green, game_loop)
        button("Quit", 512 + 200, 650, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(100)

def Menu():
    MenuExit=False
    while not MenuExit:
        gameDisplay.blit(menu,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Start", 512-200-100, 650, 100, 50, green, bright_green, game_loop)
        button("Quit", 512+200, 650, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(100)

def game_loop():
    Health = 4
    shooted1 = 0
    shooted2 = 0
    shooted3 = 0
    shooted4 = 0
    bullet_speed = 20
    Boss_x = 3000
    Boss_y = 150
    Boss_speedx = 10
    Boss_speedy = 3
    Boss_state = 1   #Boss state
    Boss_Health = 20
    Boss_ready=0
    fireball_speed = 15
    f_shooted = 0
    f_shooted2 = 0
    f_shooted3 = 0
    f_shooted4 = 0
    update = 0
    update_item_x=1300
    update_item_y=300
    health_item_x=1300
    health_item_y=300
    item_speed_x = 6
    item_speed_y = 15
    gameExit = False

    while not gameExit:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (1024, 768))
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        maskBlue = cv2.erode(maskBlue, kernel, iterations=2)
        maskBlue = cv2.dilate(maskBlue, kernel, iterations=2)
        cv2.imshow('maskBlue', maskBlue)

        centerBlue = None
        cnts = cv2.findContours(maskBlue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((xBlue, yBlue), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            centerBlue = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                mode = False
                cv2.circle(frame, centerBlue, 5, (0, 0, 255), -1)
        else:
            cx = -100
            cy = -100


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # 玩家點擊Q
                if event.key == pygame.K_q and shooted1 == 0:
                    B1 = Bullet(cx + 50, cy + 20)
                    shooted1 = 1
                    pygame.mixer.Sound.play(laser_sound)
                    pygame.time.wait(60)
                elif event.key == pygame.K_q and shooted2 == 0:
                    B2 = Bullet(cx + 50, cy + 20)
                    pygame.mixer.Sound.play(laser_sound)
                    shooted2 = 1
                    pygame.time.wait(60)
                elif event.key == pygame.K_q and shooted3 == 0:
                    B3 = Bullet(cx + 50, cy + 20)
                    pygame.mixer.Sound.play(laser_sound)
                    shooted3 = 1
                    pygame.time.wait(60)
                elif update==1 and event.key == pygame.K_q and shooted4 == 0:#升級後才有第四發
                    B4 = Bullet(cx + 50, cy + 20)
                    pygame.mixer.Sound.play(laser_sound)
                    shooted4 = 1
                    pygame.time.wait(60)
        #背景
        gameDisplay.blit(background,(0,0))
        #玩家狀態
        if Health>0:
            Player1Display(update,Health,cx,cy)
            if update==1:
                number_of_bullet = (1 - shooted1) + (1 - shooted2) + (1 - shooted3)+(1-shooted4)
                BulletDisplay(number_of_bullet)  # 子彈數量顯示
            else:
                number_of_bullet=(1-shooted1)+(1-shooted2)+(1-shooted3)
                BulletDisplay(number_of_bullet) #子彈數量顯示
        else:
            GameOver()

        #升級道具飛出
        if Boss_state==3:
            if update_item_y >550 or update_item_y <200:
                item_speed_y = -item_speed_y
            update_item_x -= item_speed_x
            update_item_y += item_speed_y
            GiveItem(update_item,update_item_x,update_item_y)
        if Boss_state==4:
            if health_item_y >550 or health_item_y <200:
                item_speed_y = -item_speed_y
            health_item_x -= item_speed_x
            health_item_y += item_speed_y
            GiveItem(health_item,health_item_x,health_item_y)

        #吃道具
        if update_item_y + 32 >= cy and update_item_y <= cy+64:
            if update_item_x <= cx+64 and update_item_x + 32 >= cx:
                update_item_x = -1000
                update=1
        if health_item_y + 32 >= cy and health_item_y <= cy + 64:
            if health_item_x <= cx + 64 and health_item_x + 32 >= cx:
                health_item_x = -1000
                Health = 4

        # 子彈飛行
        if shooted1 == 1:
            B1.now_x = B1.now_x + bullet_speed
            update_bullet(B1.now_x, B1.now_y)
            if B1.now_x >= 1024:
                shooted1 = 0
        if shooted2 == 1:
            B2.now_x = B2.now_x + bullet_speed
            update_bullet(B2.now_x, B2.now_y)
            if B2.now_x >= 1024:
                shooted2 = 0
        if shooted3 == 1:
            B3.now_x = B3.now_x + bullet_speed
            update_bullet(B3.now_x, B3.now_y)
            if B3.now_x >= 1024:
                shooted3 = 0
        if update==1 and shooted4==1:
            B4.now_x = B4.now_x + bullet_speed
            update_bullet(B4.now_x, B4.now_y)
            if B4.now_x >= 1024:
                shooted4 = 0

        #Boss位置，血量顯示
        if Boss_Health>0:
            if Boss_x>700:
                Boss_ready=0
                BossDisplay(Boss_state,Boss_x, Boss_y)
                Boss_x = Boss_x - Boss_speedx
            else:
                Boss_ready=1
                if Boss_state == 1:
                    #Boss上下移動
                    if Boss_y+512 >= 768 or Boss_y <= 110:
                        Boss_speedy =-Boss_speedy
                    Boss_y += Boss_speedy
                    BossDisplay(Boss_state,Boss_x, Boss_y)
                    BossHealthDisplay(Boss_Health,490,5)
                    #Boss開始攻擊
                    if f_shooted == 0:
                        F1 = Fireball(Boss_x, Boss_y+200)
                        f_shooted=1

                    if f_shooted == 1:
                        F1.fb_x -= fireball_speed
                        Boss_Attack(F1.fb_x, F1.fb_y)
                        if F1.fb_x <= 0 :
                            f_shooted = 0

                if Boss_state == 2:
                    # Boss上下移動
                    if Boss_y + 200 >= 750 or Boss_y <= 100:
                        Boss_speedy = -Boss_speedy
                    Boss_y += Boss_speedy
                    BossDisplay(Boss_state, Boss_x, Boss_y)
                    BossHealthDisplay(Boss_Health,490, 5)
                    # Boss開始攻擊
                    if   f_shooted == 0:
                        F1 = Fireball(Boss_x, Boss_y + 50)
                        f_shooted = 1
                    elif   f_shooted2==0 :
                        F2 = Fireball(Boss_x, Boss_y + 120)
                        f_shooted2 = 1

                    if f_shooted == 1:
                        F1.fb_x -= fireball_speed
                        Boss_Attack(F1.fb_x, F1.fb_y)
                        if F1.fb_x <= 0 :
                            f_shooted = 0
                    if f_shooted2 == 1:
                        F2.fb_x -= fireball_speed
                        Boss_Attack(F2.fb_x, F2.fb_y)
                        if F2.fb_x <= 0 :
                            f_shooted2 = 0

                if Boss_state == 3:
                    # Boss上下移動
                    if Boss_y + 400 >= 768 or Boss_y <= 110:
                        Boss_speedy = -Boss_speedy
                    Boss_y += Boss_speedy
                    BossDisplay(Boss_state,Boss_x, Boss_y)
                    BossHealthDisplay(Boss_Health,490, 5)
                    # Boss開始攻擊
                    if f_shooted == 0:
                        F1 = Fireball(Boss_x, Boss_y )
                        f_shooted = 1
                    elif  f_shooted2 == 0 :
                        F2 = Fireball(Boss_x, Boss_y + 180)
                        f_shooted2 = 1
                    elif  f_shooted3==0 :
                        F3 = Fireball(Boss_x, Boss_y + 370)
                        f_shooted3 = 1

                    if f_shooted == 1:
                        F1.fb_x -= fireball_speed
                        Boss_Attack(F1.fb_x, F1.fb_y)
                        if F1.fb_x <= 0 :
                            f_shooted = 0
                    if f_shooted2 == 1:
                        F2.fb_x -= fireball_speed
                        Boss_Attack(F2.fb_x, F2.fb_y)
                        if F2.fb_x <= 0 :
                            f_shooted2 = 0
                    if f_shooted3 == 1:
                        F3.fb_x -= fireball_speed
                        Boss_Attack(F3.fb_x, F3.fb_y)
                        if F3.fb_x <= 0 :
                            f_shooted3 = 0

                if Boss_state == 4:
                    # Boss上下移動
                    if Boss_y + 160 >= 760 or Boss_y <= 110:
                        Boss_speedy = -Boss_speedy
                    Boss_y += Boss_speedy
                    BossDisplay(Boss_state, Boss_x, Boss_y)
                    BossHealthDisplay(Boss_Health, 490, 5)
                    # Boss開始攻擊
                    if  f_shooted == 0:
                        F1 = Fireball(Boss_x, Boss_y-100)
                        f_shooted = 1
                    elif  f_shooted2 == 0 and Boss_y+50 >cx and Boss_y+50 < cx+60:
                        F2 = Fireball(Boss_x, Boss_y)
                        f_shooted2 = 1
                    elif f_shooted3 == 0:
                        F3 = Fireball(Boss_x, Boss_y + 180)
                        f_shooted3 = 1
                    elif f_shooted4==0 :
                        F4 = Fireball(Boss_x, Boss_y + 370)
                        f_shooted4 = 1

                    if f_shooted == 1:
                        F1.fb_x -= fireball_speed
                        Boss_Attack(F1.fb_x, F1.fb_y)
                        if F1.fb_x <= 0:
                            f_shooted = 0
                    if f_shooted2 == 1:
                        F2.fb_x -= fireball_speed
                        Boss_Attack(F2.fb_x, F2.fb_y)
                        if F2.fb_x <= 0:
                            f_shooted2 = 0
                    if f_shooted3 == 1:
                        F3.fb_x -= fireball_speed
                        Boss_Attack(F3.fb_x, F3.fb_y)
                        if F3.fb_x <= 0:
                            f_shooted3 = 0
                    if f_shooted4 == 1:
                        F4.fb_x -= fireball_speed
                        Boss_Attack(F4.fb_x, F4.fb_y)
                        if F4.fb_x <= 0:
                            f_shooted4 = 0


        #Boss死亡下沉
        elif Boss_Health<=0:
            BossDisplay(Boss_state,Boss_x, Boss_y)
            BossHealthDisplay(Boss_Health,490, 5)
            if Boss_y>=1200:
                Boss_x=3000
                Boss_y=200
                Boss_speedy+=3
                Boss_state+=1
                Boss_Health=20
                fireball_speed+=5
            else:
                Boss_y+=10


        #Boss受攻擊判定
        if Boss_ready==1:
            if shooted1==1 :
                if Boss_state == 1:
                    if B1.now_y + 20 > Boss_y and B1.now_y < Boss_y + 512:
                        if B1.now_x + 20 > Boss_x :
                            B1.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 2:
                    if B1.now_y + 20 > Boss_y and B1.now_y < Boss_y + 200:
                        if B1.now_x + 20 > Boss_x :
                            B1.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if  Boss_state == 3:
                    if B1.now_y + 20 > Boss_y+55 and B1.now_y < Boss_y + 120:
                        if B1.now_x + 20 > Boss_x :
                            B1.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if  Boss_state == 4:
                    if B1.now_y + 20 > Boss_y+47 and B1.now_y < Boss_y + 120:
                        if B1.now_x + 20 > Boss_x :
                            B1.now_x = 1500
                            Boss_Health = Boss_Health - 1
            if shooted2==1 :
                if Boss_state == 1:
                    if B2.now_y + 20 > Boss_y and B2.now_y < Boss_y + 512:
                        if B2.now_x + 20 > Boss_x :
                            B2.now_x=1500
                            Boss_Health=Boss_Health-1
                if Boss_state == 2:
                    if B2.now_y + 20 > Boss_y and B2.now_y < Boss_y + 200:
                        if B2.now_x + 20 > Boss_x :
                            B2.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 3:
                    if B2.now_y + 20 > Boss_y+55 and B2.now_y < Boss_y + 120:
                        if B2.now_x + 20 > Boss_x :
                            B2.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 4:
                    if B2.now_y + 20 > Boss_y+47 and B2.now_y < Boss_y + 120:
                        if B2.now_x + 20 > Boss_x :
                            B2.now_x = 1500
                            Boss_Health = Boss_Health - 1
            if shooted3==1 :
                if Boss_state == 1:
                    if B3.now_y + 20 > Boss_y and B3.now_y < Boss_y + 512:
                        if B3.now_x + 20 > Boss_x :
                            B3.now_x=1500
                            Boss_Health=Boss_Health-1
                if Boss_state == 2:
                    if B3.now_y + 20 > Boss_y and B3.now_y < Boss_y + 200:
                        if B3.now_x + 20 > Boss_x :
                            B3.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 3:
                    if B3.now_y + 20 > Boss_y + 55 and B3.now_y < Boss_y + 120:
                        if B3.now_x + 20 > Boss_x :
                            B3.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 4:
                    if B3.now_y + 20 > Boss_y + 47 and B3.now_y < Boss_y + 120:
                        if B3.now_x + 20 > Boss_x :
                            B3.now_x = 1500
                            Boss_Health = Boss_Health - 1
            if shooted4==1 :
                if Boss_state == 1:
                    if B4.now_y + 20 > Boss_y and B4.now_y < Boss_y + 512:
                        if B4.now_x + 20 > Boss_x :
                            B4.now_x=1500
                            Boss_Health=Boss_Health-1
                if Boss_state == 2:
                    if B4.now_y + 20 > Boss_y and B4.now_y < Boss_y + 200:
                        if B4.now_x + 20 > Boss_x :
                            B4.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 3:
                    if B4.now_y + 20 > Boss_y + 55 and B4.now_y < Boss_y + 120:
                        if B4.now_x + 20 > Boss_x :
                            B4.now_x = 1500
                            Boss_Health = Boss_Health - 1
                if Boss_state == 4:
                    if B4.now_y + 20 > Boss_y + 47 and B4.now_y < Boss_y + 120:
                        if B4.now_x + 20 > Boss_x :
                            B4.now_x = 1500
                            Boss_Health = Boss_Health - 1


        #玩家受到攻擊
        if Boss_Health>0 and Boss_ready==1:
            if f_shooted == 1 :
                if F1.fb_y + 24 > cy and F1.fb_y < cy + 64:
                    if F1.fb_x < cx + 64 and F1.fb_x > cx:
                        F1.fb_x = -200
                        Health-=1
            if f_shooted2 == 1 :
                if Boss_state>1:
                    if F2.fb_y + 24 > cy and F2.fb_y < cy + 64:
                        if F2.fb_x < cx + 64 and F2.fb_x > cx:
                            F2.fb_x = -200
                            Health-=1
            if f_shooted3 == 1 :
                if Boss_state > 2:
                    if F3.fb_y + 24 > cy and F3.fb_y < cy + 64:
                        if F3.fb_x < cx + 64 and F3.fb_x > cx:
                            F3.fb_x = -200
                            Health-=1
            if f_shooted4 == 1 :
                if Boss_state > 3:
                    if F4.fb_y + 24 > cy and F4.fb_y < cy + 64:
                        if F4.fb_x < cx + 64 and F4.fb_x > cx:
                            F4.fb_x = -200
                            Health-=1

        #Boss死亡重置火球位置(避免玩家撞到透明火球)
        if Boss_Health<=0:
            if Boss_state>0 and f_shooted==1:
                F1.fb_x = -200
            if Boss_state>1 and f_shooted2==1:
                F2.fb_x = -200
            if Boss_state>2 and f_shooted3==1:
                F3.fb_x = -200
            if Boss_state>3 and f_shooted4==1:
                F4.fb_x = -200


        if Boss_state==5:
            Win()

        pygame.display.update()
        clock.tick(100)


Menu()


pygame.quit()
quit()
