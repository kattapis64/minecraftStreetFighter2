# import ไลบรารี่ที่จำเป็น
import subprocess
import pygame
import sys
#กำหนด resolution
n= 10
running = True#ตัวแปรควบคุมว่าหน้าจอจะปิดหรือไม่
pygame.init()#สร้างใน pygame
game_started = False#เกมจริงยังไม่เริ่ม
screen = pygame.display.set_mode((1280,770))#สร้างหน้าจอ
pygame.display.set_caption("Minecraft Street Fighter")#กำหนดชื่อ
clock = pygame.time.Clock()#กำหนดนาฬิกา fps
background  = pygame.Surface((128*n,77*n)) #background surface

rect_gravity =0 #
#ฟังก์ชันสำหรับการเริ่มหน้าจอใหม่
def start_screen(events):#function splash screen
    global game_started # call from global
    #Load Title Screen
    splash_screen_rect = pygame.transform.scale(pygame.image.load('assets/start/title_normal'), (1280, 770))
    splash_screen_rect_rect = splash_screen_rect.get_rect()
    screen.blit(splash_screen_rect,screen.get_rect())
    #Load Start Button
    start_game_surface = pygame.transform.scale(pygame.image.load('assets/start/start_button'), (440, 160))
    start_game_rect = start_game_surface.get_rect()
    #Set position
    start_game_rect.x=1280/2-200
    start_game_rect.y=550
    #Loop through Pygame Event
    for eventd in events:
        if eventd.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if eventd.type == pygame.MOUSEBUTTONDOWN and eventd.button == 1:
            if start_game_rect.collidepoint(eventd.pos):
                #Check Click
                game_started = True
    #create screen start button
    screen.blit(start_game_surface,start_game_rect)
#================ฟังก์ชันสำหรับหน้าเลือกตัวละคร=====================
def choosechar(events):
    global player1,player2
    #initialize icons for choosing
    #Background
    bg_surf = pygame.transform.scale(pygame.image.load('assets/map/characterselect_bg_3'), (1280, 770))
    bg_rect = bg_surf.get_rect()
    screen.blit(bg_surf,bg_rect)
    #Happy Ghast for player1
    char1_p1 = pygame.transform.scale(pygame.image.load('assets/map/happyghast_prev'), (210, 210))
    char1_p1_rect = char1_p1.get_rect(topleft=(110,250))
    #blaze for player1
    char2_p1 = pygame.transform.scale(pygame.image.load('assets/map/blaze_prev'), (210, 210))
    char2_p1_rect = char2_p1.get_rect(topleft=(370,250))
    #vindicator for player1
    char3_p1 =pygame.transform.scale(pygame.image.load('assets/map/vindicator_prev'), (210, 210))
    char3_p1_rect = char3_p1.get_rect(topleft=(650,250))

    #happy ghast player 2
    char1_p2 =pygame.transform.scale(pygame.image.load('assets/map/happyghast_prev'), (210, 210))
    char1_p2_rect = char1_p2.get_rect(topleft=(110,500))
    #blaze for player 2
    char2_p2 = pygame.transform.scale(pygame.image.load('assets/map/blaze_prev'), (210, 210))
    char2_p2_rect = char2_p2.get_rect(topleft=(370,500))
    #vindicator player 2
    char3_p2 = pygame.transform.scale(pygame.image.load('assets/map/vindicator_prev'), (210, 210))
    char3_p2_rect = char3_p2.get_rect(topleft=(650,520))
    #loop through event finding mouse click
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and map_choice is None:#if havent choosen map
            if char1_p1_rect.collidepoint(event.pos):
                print("P1 Chose 1")
                player1= '1'
                char1_p1.fill('black')#for click effect
            elif char2_p1_rect.collidepoint(event.pos):
                print("P1 Chose 2")
                player1= '2'
                char2_p1.fill('black')

            elif char3_p1_rect.collidepoint(event.pos):
                print("P1 Chose 3")
                player1= '3'
                char3_p1.fill('black')

            elif char1_p2_rect.collidepoint(event.pos):
                print("P2 Chose 1")
                player2= '1'
                char1_p2.fill('black')

            elif char2_p2_rect.collidepoint(event.pos):
                print("P2 Chose 2")
                player2= '2'
                char2_p2.fill('black')

            elif char3_p2_rect.collidepoint(event.pos):
                print("P2 Chose 3")
                char3_p2.fill('black')

                player2= '3'
    #create icons
    screen.blit(char1_p1,char1_p1_rect)
    screen.blit(char2_p1,char2_p1_rect)
    screen.blit(char3_p1,char3_p1_rect)
    screen.blit(char1_p2,char1_p2_rect)
    screen.blit(char2_p2,char2_p2_rect)
    screen.blit(char3_p2,char3_p2_rect)
#=============function สำหรับการเลือกพื้นหลัว====================================
def choosemap(events):
    global map_choice
    screen.fill('black')
    img_map = pygame.transform.scale(pygame.image.load('assets/maps_selection/map'), (1288, 770))
    img_map_rect = img_map.get_rect()
    screen.blit(img_map,img_map_rect)
    map1 = pygame.transform.scale(pygame.image.load('assets/maps_selection/overworld_map'), (420, 480))

    map1_rect = map1.get_rect(topleft=(170,210))

    map2 = pygame.transform.scale(pygame.image.load('assets/map/nether_mapselect'), (420, 480))
    map2_rect = map2.get_rect(topleft=(170+520,210))

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and map_choice is None and player1 and player2:
            if map1_rect.collidepoint(event.pos):
                print("Map 1 chosen")
                map_choice=1
            elif map2_rect.collidepoint(event.pos):
                print("Map 2 chosen")
                map_choice=2

    screen.blit(map1,map1_rect)
    screen.blit(map2,map2_rect)
#=================Function แรกสำหรับการสร้างหน้าจอ pygame สำหรับการเลือกต่างๆ===============
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and test_rect.bottom==700:
                rect_gravity = -20

    rect_gravity+=1
    #Call Previous functions
    if not game_started:
        start_screen(events)
        player1=None#set for player 1 and 2
        player2=None
    elif game_started: # will be executed if hit gamestart
        if player1 is None or player2 is None:
            screen.fill('black')#clear screen
            choosechar(events)
            map_choice=None
        elif map_choice is None:# will be executed after chosing character
            screen.fill('black')
            choosemap(events)
        else: # if chosen all; will stop
            running = False

    pygame.display.update()
    clock.tick(60)

#สร้างหน้า pygame เกมจริง
pygame.init()
n=10 #กำหนดความละเอียดภาพ
screen = pygame.display.set_mode((1280,770))#สร้างหน้าจอ
pygame.display.set_caption("Minecraft Street Fighter")#กำหนดชื่อ
clock = pygame.time.Clock()#กำหนดนาฬิกาตั้งค่าเฟรม
movement_speed = 50#กำหนดความเร็วการเคลื่อนที่

health_player1 = 100#กำหนดพลังชีวิตเริ่มต้นสำหรับผู้เล่นที่ 1
health_player2 = 100#กำหนดพลังชีวิตเริ่มต้นสำหรับผู้เล่นที่ 2
energy_player1 = 100#กำหนดพลังงานเริ่มต้นสำหรับผู้เล่นที่ 1
energy_player2 = 100#กำหนดพลังงานเริ่มต้นสำหรับผู้เล่นที่ 2


#กำหนดค่าการนั่งเริ่มต้น
crouched_p1 = False
crouched_p2 = False
#สร้าง fireball projectile สำหรับ player 1
fireball_surf = pygame.transform.scale(pygame.image.load('assets/Fireball.png').convert_alpha(), (120, 120))
show_fireball_rect= False
fireball_rect = fireball_surf.get_rect()
#สร้าง fireball projectile สำหรับ player 1
fireball_surf2 = pygame.transform.scale(pygame.image.load('assets/Fireball.png').convert_alpha(), (120, 120))
show_fireball_rect2= False
fireball_rect2 = fireball_surf2.get_rect()

#สร้าง snow projectile สำหรับ player 1
snowball_surf = pygame.transform.scale(pygame.image.load('assets/Snowball.png').convert_alpha(), (120, 120))
show_snowball_rect= False
snowball_rect = snowball_surf.get_rect()
#สร้าง snow projectile สำหรับ player 2
snowball_surf2 = pygame.transform.scale(pygame.image.load('assets/Snowball.png').convert_alpha(), (120, 120))
show_snowball_rect2= False
snowball_rect2 = snowball_surf.get_rect()

#สร้าง arrow projectile สำหรับ player 1
arrow_surf = pygame.transform.scale(pygame.image.load('assets/Arrow.png').convert_alpha(), (200, 60))
show_arrow = False
arrow_rect = arrow_surf.get_rect()
#สร้าง arrow projectile สำหรับ player 2
arrow_surf2 = pygame.transform.scale(pygame.image.load('assets/Arrow.png').convert_alpha(), (200, 60))
show_arrow2 = False
arrow_rect2 = arrow_surf.get_rect()
#สร้าง Laser projectile สำหรับ player 1
laser_surf = pygame.transform.scale(pygame.image.load('assets/Laser_beam.png').convert_alpha(), (3200, 90))
show_laser = False
laser_rect = laser_surf.get_rect()
#สร้าง Laser projectile สำหรับ player 2
laser_surf2 = pygame.transform.scale(pygame.image.load('assets/Laser_beam.png').convert_alpha(), (3200, 90))
show_laser2 = False
laser_rect2 = laser_surf2.get_rect()
#สร้าง RODS projectile สำหรับ player 1
rods_surf =pygame.transform.scale(pygame.image.load('assets/Throw_rods.png').convert_alpha(), (188 * 4, 54 * 4))
show_rods = False
rods_rect = rods_surf.get_rect()
#สร้าง RODS projectile สำหรับ player 2
rods_surf2 = pygame.transform.scale(pygame.image.load('assets/Throw_rods.png').convert_alpha(), (188 * 4, 54 * 4))
show_rods2 = False
rods_rect2 = rods_surf2.get_rect()
#================Counter and States สำหรับการแสดงผล Animation===================
counter_ghast_header_p1=0
ghast_header_p1 = False
counter_ghast_laser_p1=0
ghast_laser_p1 = False
counter_ghast_snow_p1 =0
ghast_snow_p1= False


counter_blaze_hit_p1=0
blaze_hit_p1 = False
counter_blaze_throw_p1 =0
blaze_throw_p1 = False
counter_blaze_throw_all_p1=0
blaze_throw_all_p1 = False

counter_ghast_header_p1=0
counter_ghast_laser_p1=0
counter_ghast_snow_p1 =0
ghast_header_p1 = False
counter_pillager_axe_p1 =0
pillager_axe_p1 = False
counter_pillager_cr_p1=0
pillager_cr_p1 = False
counter_ravager_p1=0
ravager_p1 = False


counter_blaze_hit_p2=0
blaze_hit_p2 = False
counter_blaze_throw_p2 =0
blaze_throw_p2 = False
counter_blaze_throw_all_p2=0
blaze_throw_all_p2 = False

counter_ghast_header_p2=0
ghast_header_p2 = False
counter_ghast_laser_p2=0
ghast_laser_p2 = False
counter_ghast_snow_p2 =0
ghast_snow_p2= False

counter_pillager_axe_p2 =0
pillager_axe_p2 = False
counter_pillager_cr_p2=0
pillager_cr_p2 = False
counter_ravager_p2=0
ravager_p2 = False


#=============================เลือกไฟล์ภาพตัวละครจาก ตัวแปร  player 1 และ player2==============
if player1 == '1':
    icon1 = pygame.transform.scale(pygame.image.load("assets/map/happyghast_prev").convert_alpha(), (108 * 4.5, 112 * 4.5))
    player1Surf = pygame.transform.scale(pygame.image.load("assets/Happy_Ghast.png").convert_alpha(), (108 * 6, 112 * 6))
if player1 == '2':
    player1Surf = pygame.transform.scale(pygame.image.load("assets/Blaze.png").convert_alpha(), (164 * 2, 232 * 2))
    icon1 = pygame.transform.scale(pygame.image.load("assets/map/blaze_prev").convert_alpha(), (120, 120))
if player1 == '3':
    player1Surf = pygame.transform.scale(pygame.image.load("assets/Pillager.png").convert_alpha(), (148 * 2, 238 * 2))
    icon1 = pygame.transform.scale(pygame.image.load("assets/map/vindicator_prev").convert_alpha(), (120, 120))
if player2 == '1':
    player2Surf = pygame.transform.scale(pygame.image.load("assets/Happy_Ghast.png").convert_alpha(), (108 * 4.5, 112 * 4.5))
    icon2 = pygame.transform.scale(pygame.image.load("assets/map/happyghast_prev").convert_alpha(), (120, 120))
if player2 == '2':
    player2Surf = pygame.transform.scale(pygame.image.load("assets/Blaze.png").convert_alpha(), (164 * 2, 232 * 2))
    icon2 = pygame.transform.scale(pygame.image.load("assets/map/blaze_prev").convert_alpha(), (120, 120))
if player2 == '3':
    player2Surf = pygame.transform.scale(pygame.image.load("assets/Pillager.png").convert_alpha(), (148 * 2, 238 * 2))
    icon2 = pygame.transform.scale(pygame.image.load("assets/map/vindicator_prev").convert_alpha(), (120, 120))

#สร้าง rect ตัวละครทั้งสอง
player1Rect = player1Surf.get_rect()
player2Rect = player2Surf.get_rect()
#สร้าง icon แสดงผล
icon1_rect = icon1.get_rect()
icon1_rect.x = 750
icon2_rect = icon2.get_rect()
icon2_rect.x = 400
icon2_rect.y = 50
icon1_rect.y = 50
player1Rect.x= 1100

rect_gravity1 =0
rect_gravity2 =0

#set state เอาไว้ดูว่าโดน damage หรือไม่
prev_health_p1 = health_player1
prev_health_p2 = health_player2

ko_surf = pygame.transform.scale(pygame.image.load('assets/map/KO'), (920, 400))
ko_rect = ko_surf.get_rect()
ko_rect.x = 190
ko_rect.y = 180
#หน้าจอชนะของ player1
victoryp1_surf = pygame.transform.scale(pygame.image.load('assets/map/victoryscreen1.png'), (740, 500))
victoryp1_rect = victoryp1_surf.get_rect()
victoryp1_rect.x = 270
victoryp1_rect.y = 140
#หน้าจอชนะของ player2
victoryp2_surf = pygame.transform.scale(pygame.image.load('assets/map/victoryscreen2.png'), (740, 500))
victoryp2_rect = victoryp1_surf.get_rect()
victoryp2_rect.x = 270
victoryp2_rect.y = 140
#ปุ่ม restart สำหรับ player
restart_surf = pygame.transform.scale(pygame.image.load('assets/map/restart_button'), (220, 80))
restart_rect = restart_surf.get_rect()
restart_rect.x = 400
restart_rect.y = 650
#ปุ่ม quit สำหรับ player
quit_surf = pygame.transform.scale(pygame.image.load('assets/map/exit_button'), (220, 80))
quit_rect = quit_surf.get_rect()
quit_rect.x = 700
quit_rect.y = 650

#main game loop
while True:
    # โหลดแบกราวตามแมพที่เลือก
    if map_choice == 1:
        background = 'assets/map/overworld_mapbg'
    elif map_choice == 2:
        background = 'assets/map/nether_mapbg'
    #โหลด icon จาก player
    if player1 == '1':
        icon1 = pygame.transform.scale(pygame.image.load("assets/map/happyghast_prev").convert_alpha(), (120, 120))
    if player1 == '2':
        icon1 = pygame.transform.scale(pygame.image.load("assets/map/blaze_prev").convert_alpha(), (120, 120))
    if player1 == '3':
        icon1 = pygame.transform.scale(pygame.image.load("assets/map/vindicator_prev").convert_alpha(), (120, 120))
    if player2 == '1':
        icon2 = pygame.transform.scale(pygame.image.load("assets/map/happyghast_prev").convert_alpha(), (120, 120))
    if player2 == '2':
        icon2 = pygame.transform.scale(pygame.image.load("assets/map/blaze_prev").convert_alpha(), (120, 120))
    if player2 == '3':
        icon2 = pygame.transform.scale(pygame.image.load("assets/map/vindicator_prev").convert_alpha(), (120, 120))
    background_surf = pygame.transform.scale(pygame.image.load(background),(1280,770))
    background_rect = background_surf.get_rect()
    #draw background
    screen.blit(background_surf,background_rect )
    #การฟื้นฟูของพลังชีวิตและพลังงาน
    health_player1 +=15/60
    health_player2 +=15/ 60
    energy_player1 += 30/ 60
    energy_player2 += 30/ 60
    #cap health and energy
    if health_player1 > 100:
        health_player1 =100
    if health_player2 > 100:
        health_player2 =100
    if energy_player1 > 100:
        energy_player1 =100
    if energy_player2 > 100:
        energy_player2 =100
    screen.blit(icon1, icon1_rect)
    screen.blit(icon2, icon2_rect)

    #check ให้ตัวละคนหันซ้ายขวา เข้าหาคู้ต่อสู้
    if player1 =='1':
        if player2Rect.x <player1Rect.x:
            player1Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                "assets/Happy_Ghast.png").convert_alpha(),
                                                                       (108 * 4.5, 112 * 4.5)),True,False)
        else:
            player1Surf = pygame.transform.scale(pygame.image.load(
                "assets/Happy_Ghast.png").convert_alpha(),(108 * 4.5, 112 * 4.5))


    elif player1 =='2':
        if player1Rect.x < player2Rect.x:
            player1Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                "assets/Blaze.png").convert_alpha(),
                                                                       (164 * 2, 232 * 2)),True,False)
        else:
            player1Surf = pygame.transform.scale(pygame.image.load(
                "assets/Blaze.png").convert_alpha(),
                                                                       (164 * 2, 232 * 2))

    elif player1 =='3':
        if player1Rect.x < player2Rect.x:
            player1Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                "assets/Pillager.png").convert_alpha(),
                                                                       (148 * 2, 238 * 2)),True,False)
        else:
            player1Surf = pygame.transform.scale(pygame.image.load(
                "assets/Pillager.png").convert_alpha(),
                                   (148 * 2, 238 * 2))

    if player2 == '1':
        if player2Rect.x > player1Rect.x:
            player2Surf = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load("assets/Happy_Ghast.png").convert_alpha(),
                                       (108 * 4.5, 112 * 4.5)), True, False)
        else:
            player2Surf = pygame.transform.scale(pygame.image.load("assets/Happy_Ghast.png").convert_alpha(),
                                       (108 * 4.5, 112 * 4.5))

    elif player2 == '2':
        if player1Rect.x > player2Rect.x:
            player2Surf = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load("assets/Blaze.png").convert_alpha(),
                                       (164 * 2, 232 * 2)), True, False)
        else:
            player2Surf =pygame.transform.scale(pygame.image.load("assets/Blaze.png").convert_alpha(),
                                       (164 * 2, 232 * 2))

    elif player2 == '3':
        if player1Rect.x > player2Rect.x:
            player2Surf = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load("assets/Pillager.png").convert_alpha(),
                                       (148 * 2, 238 * 2)), True, False)
        else:
            player2Surf =pygame.transform.scale(pygame.image.load("assets/Pillager.png").convert_alpha(),
                                       (148 * 2, 238 * 2))
    #=================code การเคลื่อนที่ของ projectile ต่างๆ===================
    if player1 =='1':
        if show_snowball_rect and energy_player1 >8:

            if snowball_rect.colliderect(player2Rect):
                health_player2 -= 7.5
            energy_player1 -= 1
            if player1Rect.x >player2Rect.x:
                snowball_rect.x-=300
            else:
                snowball_rect.x += 300
            snowball_rect.y = player1Rect.y+200

    elif player1 =='2'and energy_player1 >8:
        if show_fireball_rect:
            if fireball_rect.colliderect(player2Rect):
                health_player2 -= 7.5
            energy_player1 -= 1
            if player1Rect.x >player2Rect.x:
                fireball_rect.x-=100
            else:
                fireball_rect.x += 100
            fireball_rect.y = player1Rect.y
    elif player1 == '3'and energy_player1 >8:
        if show_arrow:
            if arrow_rect.colliderect(player2Rect):
                health_player2 -= 7.5
            energy_player1 -= 1
            if player1Rect.x > player2Rect.x:
                arrow_rect.x -= 100
            else:
                arrow_rect.x += 100
            arrow_rect.y = player1Rect.y+150

    if player2 =='1'and energy_player2 >8:
        if show_snowball_rect2:
            if snowball_rect2.colliderect(player1Rect):
                health_player1 -= 7.5
            energy_player2 -= 1
            if player1Rect.x > player2Rect.x:
                snowball_rect2.x += 300
            else:
                snowball_rect2.x -= 300
            snowball_rect2.y = player2Rect.y+200
    if player2 =='2'and energy_player2>8:
        if show_fireball_rect2:
            if fireball_rect2.colliderect(player1Rect):
                health_player1 -= 7.5
            energy_player2 -= 1
            if player1Rect.x > player2Rect.x:
                fireball_rect2.x += 150
            else:
                fireball_rect2.x -= 150
            fireball_rect2.y = player2Rect.y +100
    if player2 =='3'and energy_player2 >8:
        if show_arrow2:
            if arrow_rect2.colliderect(player1Rect):
                health_player1 -= 7.5
            energy_player2 -= 1
            if player1Rect.x > player2Rect.x:
                arrow_rect2.x += 100
            else:
                arrow_rect2.x -= 100
            arrow_rect2.y = player2Rect.y+150
    if player2 =='1' and show_laser:
        if laser_rect.colliderect(player1Rect):
            health_player1 -= 5
        energy_player2 -= 8
        if player1Rect.x > player2Rect.x:
            laser_rect.x += 500
        else:
            laser_rect.x -= 500
        if player2Rect.y +100!=0:
            laser_rect.y = player2Rect.y +100

    if player1 =='1' and show_laser2:
        if laser_rect2.colliderect(player2Rect):
            health_player2 -= 5
        energy_player1 -= 8
        if player1Rect.x > player2Rect.x:
            laser_rect2.x -= 200
        else:
            laser_rect2.x += 200
        laser_rect2.y = player1Rect.y + 100

    if player1 =='2' and show_rods and energy_player1 >0:
        if rods_rect.colliderect(player2Rect):
            health_player2 -= 4
        energy_player1 -= 5
        if player1Rect.x > player2Rect.x:
            rods_rect.x -= 200
        else:
            rods_rect.x += 200
        rods_rect.y = player1Rect.y+120

    if player2 =='2' and show_rods2 and energy_player2 >0:
        if rods_rect2.colliderect(player1Rect):
            health_player1 -= 4
        energy_player2 -= 5
        if player1Rect.x > player2Rect.x:
            rods_rect2.x += 200
        else:
            rods_rect2.x -= 200
        rods_rect2.y = player2Rect.y+120

    #load รูปของค่าพลังชีวิตและพลังงาน
    if health_player2 > 90:
        health_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/health/100'), (400, 80)), True, False)
    elif health_player2 > 75:
        health_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/health/75'), (400, 80)), True, False)
    elif health_player2 > 50:
        health_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/health/50'), (400, 80)), True, False)
    elif health_player2 > 25:
        health_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/health/25'), (400, 80)), True, False)
    elif health_player2 > 0:
        health_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/health/0'), (400, 80)), True, False)
    if health_player1 > 90:
        health_surf2 = pygame.transform.scale(pygame.image.load('assets/health/100'), (400, 80))
    elif health_player1 > 75:
        health_surf2 = pygame.transform.scale(pygame.image.load('assets/health/75'), (400, 80))
    elif health_player1 > 50:
        health_surf2 = pygame.transform.scale(pygame.image.load('assets/health/50'), (400, 80))
    elif health_player1 > 25:
        health_surf2 = pygame.transform.scale(pygame.image.load('assets/health/25'), (400, 80))
    elif health_player1 > 0:
        health_surf2 = pygame.transform.scale(pygame.image.load('assets/health/0'), (400, 80))


    if energy_player2 > 90:
        energy_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/energy/100'), (500, 100)), True, False)
    elif energy_player2 > 75:
        energy_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/energy/75'), (500, 100)), True, False)
    elif energy_player2 > 50:
        energy_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/energy/50'), (500, 100)), True, False)
    elif energy_player2 > 25:
        energy_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/energy/25'), (500, 100)), True, False)
    elif energy_player2 > 0:
        energy_surf1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/energy/0'), (500, 100)), True, False)
    if energy_player1 > 90:
        energy_surf2 = pygame.transform.scale(pygame.image.load('assets/energy/100'), (500, 100))
    elif energy_player1 > 75:
        energy_surf2 = pygame.transform.scale(pygame.image.load('assets/energy/75'), (500, 100))
    elif energy_player1 > 50:
        energy_surf2 = pygame.transform.scale(pygame.image.load('assets/energy/50'), (500, 100))
    elif energy_player1 > 25:
        energy_surf2 = pygame.transform.scale(pygame.image.load('assets/energy/25'), (500, 100))
    elif energy_player1 > 0:
        energy_surf2 = pygame.transform.scale(pygame.image.load('assets/energy/0'), (500, 100))
        #===========================================================================================
    #แสดงผลค่าพลังงาน
    health_rect1 = health_surf1.get_rect()
    health_rect2 = health_surf2.get_rect()
    health_rect2.x = 1280 - 400

    energy_rect1 = energy_surf1.get_rect()
    energy_rect2 = energy_surf2.get_rect()
    energy_rect2.x = 1280 - 400
    energy_rect1.y = 100
    energy_rect1.x = -100
    energy_rect2.y = 100

    keys = pygame.key.get_pressed()
    screen.blit(health_surf1, health_rect1)
    screen.blit(health_surf2, health_rect2)

    screen.blit(energy_surf1, energy_rect1)
    screen.blit(energy_surf2, energy_rect2)

    #gravity
    rect_gravity1+=10
    rect_gravity2+=10
    player1Rect.y += rect_gravity1
    player2Rect.y += rect_gravity2
    #flip arrow projectil based on position relative to enemy
    if player1Rect.x > player2Rect.x:
        arrow_surf2 = pygame.transform.flip(
            pygame.transform.scale(pygame.image.load('assets/Arrow.png').convert_alpha(), (200, 60)), True, False)
    if player1Rect.x <player2Rect.x:
            arrow_surf2 = pygame.transform.scale(pygame.image.load('assets/Arrow.png').convert_alpha(), (200, 60))
    #set floor
    if player1Rect.y >250:player1Rect.y=250
    if player2Rect.y > 250: player2Rect.y =250

    for event in pygame.event.get():
        #the following code will play skill based on which key is pressed
            #movement includes wasd for player2
            # arrow keys for player1
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)
            #detect crouch player2
            if event.key == pygame.K_s:
                crouched_p2 = True
            #ignore up an down at same time
            if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
                pass
            #detect jump player1
            elif event.key == pygame.K_UP and player1Rect.y==250:
                rect_gravity1 = -70
            #detect crouch player 1
            elif event.key == pygame.K_DOWN:
                crouched_p1 = True
            #ignore up and down at the same time
            if keys[pygame.K_w] and keys[pygame.K_s]:
                continue
                # detect jump player 2
            elif event.key == pygame.K_w and player2Rect.y == 250:
                rect_gravity2 = -70


            #Comma detection for melee skill player 1
            elif event.key == pygame.K_COMMA :
                if player1Rect.colliderect(player2Rect):
                    if player1=='1':
                        ghast_header_p1 = True
                        energy_player1 -= 10
                        health_player2-=8
                    elif player1=='2':
                        blaze_hit_p1 = True
                        health_player2-=8
                    elif player1=='3':
                        pillager_axe_p1 = True
                        health_player2-=8
            # Period detection for ranged skill player 1
            elif event.key == pygame.K_PERIOD:
                show_proj_1 = True
                if player1 =='1':
                    show_snowball_rect = True
                    ghast_snow_p1 = True
                if player1 =='2':
                    show_fireball_rect = True
                    blaze_throw_p1 = True
                if player1=='3':
                    show_arrow =True
                    pillager_cr_p1 = True
            # SLASH detection for ultimate skill player 1
            elif (event.key == pygame.K_SLASH) and (energy_player1>0) and (player1 == '1') :
                show_laser2=True
                ghast_laser_p1 = True
            elif (event.key == pygame.K_SLASH) and (energy_player1>0) and (player1 == '2') :
                show_rods=True
                blaze_throw_all_p1 = True
            elif (event.key == pygame.K_SLASH) and (energy_player1 > 0) and (player1 == '3'):
                show_laser = False
                show_laser2 = False
                if player1Rect.x > player2Rect.x:
                    player1Rect.x = player2Rect.x + 200
                else:
                    player1Rect.x = player2Rect.x - 200
                ravager_p1 = True

                health_player2 -= 30
                energy_player1 -= 50
            # q detection for melee skill player 2
            elif event.key == pygame.K_q :
                if player1Rect.colliderect(player2Rect):
                    if player2=='1':
                        ghast_header_p2 = True
                        energy_player2 -= 10
                        health_player1-=8
                    elif player2=='2':
                        blaze_hit_p2 = True
                        health_player1-=8
                    elif player2=='3':
                        pillager_axe_p2 = True
                        health_player1-=8
            # e detection for ranged skill player 2
            elif event.key == pygame.K_e:

                if player2 =='1':
                    show_snowball_rect2 = True
                    ghast_snow_p2 = True

                if player2 =='2':
                    show_fireball_rect2 = True
                    blaze_throw_p2 = True
                if player2=='3':
                    show_arrow2 =True
                    pillager_cr_p2 = True
            # r detection for ultimate skill player 2
            if event.key == pygame.K_r and player2 == '1' and energy_player2>80:
                show_laser = True
                ghast_laser_p2 = True
            if event.key == pygame.K_r and player2 == '2' and energy_player2>80:
                show_rods2 = True
                blaze_throw_all_p2 = True
            if event.key == pygame.K_r and player2 == '3' and energy_player2>40:
                show_laser = False
                show_laser2 = False
                if player1Rect.x>player2Rect.x:
                    player2Rect.x = player1Rect.x-800
                else:
                    player2Rect.x = player1Rect.x-800
                ravager_p2 = True

                health_player1-=30
                energy_player2-=50
        # finishing job when key was unpressed or lifted
        # set animation states to FALSE for all
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and player1Rect.y == 250:
                crouched_p1 = False
            if event.key == pygame.K_s:
                crouched_p2 = False


            if event.key == pygame.K_SLASH and player1=='1':
                show_laser2 = False
                laser_rect2.x = player1Rect.x
                ghast_laser_p1=False
            if event.key == pygame.K_SLASH and player1=='2':
                show_rods = False
                rods_rect.x = player1Rect.x
                blaze_throw_all_p1 = False
            if event.key == pygame.K_SLASH and player1=='3':
                ravager_p1 = False
                ravager_p2=False

            if event.key == pygame.K_PERIOD:
                if player1 =='1':
                    show_snowball_rect = False
                    snowball_rect.x = player1Rect.x
                    ghast_snow_p1 = False
                if player1=='2':
                    show_fireball_rect = False
                    fireball_rect.x = player1Rect.x
                    blaze_throw_p1 = False
                if player1=='3':
                    show_arrow = False
                    arrow_rect.x = player1Rect.x
                    pillager_cr_p1=False

            if event.key == pygame.K_COMMA and player1 == '1':
                show_laser2 = False
                laser_rect2.x = player1Rect.x
                ghast_header_p1 = False
            if event.key == pygame.K_COMMA and player1 == '2':
                show_rods1 = False
                rods_rect.x = player1Rect.x

                blaze_throw_all_p1 = False
            if event.key == pygame.K_COMMA and player1 == '3':
                ravager_p1 = False

            if event.key == pygame.K_q:
                if player2 == '1':
                    ghast_header_p2 = False
                elif player2 == '2':
                    blaze_hit_p2 = False
                elif player2 == '3':
                    pillager_axe_p2 = False

            if event.key == pygame.K_e:
                if player2 =='1':
                    show_snowball_rect2 = False
                    snowball_rect2.x = player2Rect.x
                    ghast_snow_p2 = False
                if player2=='2':
                    show_fireball_rect2= False
                    fireball_rect2.x = player2Rect.x
                    blaze_throw_p2 = False
                if player2=='3':
                    show_arrow2 = False
                    arrow_rect2.x = player2Rect.x
                    pillager_cr_p2 = False

            if event.key == pygame.K_r and player2 == '1':
                show_laser = False
                laser_rect.x = player2Rect.x
                ghast_laser_p2 = False
            if event.key == pygame.K_r and player2 == '2':
                show_rods2 = False
                rods_rect.x = player2Rect.x

                blaze_throw_all_p2 = False
            if event.key == pygame.K_r and player2 == '3':
                ravager_p2 = False
    #for movement key ; outside loop to be able to hold
    if keys[pygame.K_RIGHT]:
        player1Rect.x += movement_speed
        if player1Rect.x > 128*n:
            player1Rect.x = 128*n-player1Rect.width


    if keys[pygame.K_LEFT]:
        player1Rect.x -= movement_speed

        if player1Rect.x <-1:
            player1Rect.x = 1

    if keys[pygame.K_d]:
        player2Rect.x += movement_speed
        if player2Rect.x > 128 * n:
            player2Rect.x = 128 * n-player2Rect.width

    if keys[pygame.K_a]:
        player2Rect.x -= movement_speed
        if player2Rect.x <-1:
            player2Rect.x = 1
    #display projectile if the boolean value to show is true
    if show_fireball_rect:
        screen.blit(fireball_surf, fireball_rect)
    if show_snowball_rect:
        screen.blit(snowball_surf, snowball_rect)
    if show_arrow:
        screen.blit(arrow_surf, arrow_rect)
    if show_fireball_rect2:
        screen.blit(fireball_surf2, fireball_rect2)
    if show_snowball_rect2:
        screen.blit(snowball_surf2, snowball_rect2)
    if show_arrow2:
        screen.blit(arrow_surf2, arrow_rect2)
    if show_laser:
        screen.blit(laser_surf, laser_rect)
    if show_laser2:
        screen.blit(laser_surf2, laser_rect2)
    if show_rods:
        screen.blit(rods_surf,rods_rect)
    if show_rods2:
        screen.blit(rods_surf2,rods_rect2)
    # ==================================Animation Player 1========================================

    if ghast_header_p1:
        counter_ghast_header_p1 += 12
        if player1Rect.x < player2Rect.x:
            if counter_ghast_header_p1 % 60 < 12:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header1.png"),
                                                     (212 * 4, 208 * 4))
            elif counter_ghast_header_p1 % 60 < 24:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header2.png"),
                                                     (212 * 4, 208 * 4))
            elif counter_ghast_header_p1 % 60 < 36:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header3.png"),
                                                     (212 * 4, 208 * 4))
            elif counter_ghast_header_p1 % 60 < 48:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header4.png"),
                                                     (212 * 4, 208 * 4))
            elif counter_ghast_header_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header5.png"),
                                                     (212 * 4, 208 * 4))
            health_player2 -= 2
        else:
            if counter_ghast_header_p1 % 60 < 12:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_header1.png"),
                                           (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p1 % 60 < 24:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_header2.png"),
                                           (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p1 % 60 < 36:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_header3.png"),
                                           (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p1 % 60 < 48:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_header4.png"),
                                           (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_header5.png"),
                                           (212 * 4, 208 * 4)), True, False)
            health_player2 -= 2

    if ghast_snow_p1:
        counter_ghast_snow_p1 += 12
        if player1Rect.x < player2Rect.x:
            if counter_ghast_snow_p1 % 60 < 30:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_snow1.png"),
                                                     (108 * 4.5, 112 * 4.5))
            elif counter_ghast_snow_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_snow2.png"),
                                                     (108 * 4.5, 112 * 4.5))
        else:
            if counter_ghast_snow_p1 % 60 < 30:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_snow1.png"),
                                           (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_snow_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_snow2.png"),
                                           (108 * 4.5, 112 * 4.5)), True, False)
    if ghast_laser_p1:
        counter_ghast_laser_p1 += 10

        if player1Rect.x < player2Rect.x:
            if counter_ghast_laser_p1 % 60 < 15:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser1.png"),
                                                     (108 * 4.5, 112 * 4.5))
            elif counter_ghast_laser_p1 % 60 < 30:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser2.png"),
                                                     (108 * 4.5, 112 * 4.5))
            elif counter_ghast_laser_p1 % 60 < 45:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser2.png"),
                                                     (108 * 4.5, 112 * 4.5))
            elif counter_ghast_laser_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser4.png"),
                                                     (108 * 4.5, 112 * 4.5))
        else:
            if counter_ghast_laser_p1 % 60 < 15:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser1.png"),
                                           (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_laser_p1 % 60 < 30:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser2.png"),
                                           (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_laser_p1 % 60 < 45:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser2.png"),
                                           (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_laser_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser4.png"),
                                           (108 * 4.5, 112 * 4.5)), True, False)
    if blaze_hit_p1:
        counter_blaze_hit_p1 += 12
        if player1Rect.x >player2Rect.x:
            if counter_blaze_hit_p1 % 60 < 20:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit1.png"),
                                                     (136 * 4, 116 * 4))
            elif counter_blaze_hit_p1 % 60 < 40:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit2.png"),
                                                     (136 * 4, 116 * 4))
            elif counter_blaze_hit_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit3.png"),
                                                     (136 * 4, 116 * 4))
            health_player2 -= 2
        else:
            if counter_blaze_hit_p1 % 60 < 20:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit1.png"),
                                           (136 * 4, 116 * 4)), True, False)
            elif counter_blaze_hit_p1 % 60 < 40:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit2.png"),
                                           (136 * 4, 116 * 4)), True, False)
            elif counter_blaze_hit_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit3.png"),
                                           (136 * 4, 116 * 4)), True, False)
            health_player2 -= 2
    if blaze_throw_p1:
        counter_blaze_throw_p1 += 12
        if player1Rect.x > player2Rect.x:
            if counter_blaze_throw_p1 % 60 < 12:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_p1 % 60 < 24:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_p1 % 60 < 36:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_p1 % 60 < 48:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"),
                                                     (82 * 4, 128 * 4))
            health_player2 -= 2
        else:
            if counter_blaze_throw_p1 % 60 < 12:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p1 % 60 < 24:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p1 % 60 < 36:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p1 % 60 < 48:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"),
                                           (82 * 4, 128 * 4)), True, False)
            health_player2 -= 2
    if blaze_throw_all_p1:
        counter_blaze_throw_all_p1 += 12
        rods_rect.y = player1Rect.y + 100
        if player1Rect.x > player2Rect.x:
            if counter_blaze_throw_all_p1 % 60 < 12:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p1 % 60 < 24:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p1 % 60 < 36:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p1 % 60 < 48:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"),
                                                     (82 * 4, 128 * 4))
        else:
            if counter_blaze_throw_all_p1 % 60 < 12:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p1 % 60 < 24:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p1 % 60 < 36:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p1 % 60 < 48:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"),
                                           (82 * 4, 128 * 4)), True, False)

    if pillager_axe_p1:
        counter_pillager_axe_p1 += 12
        if player1Rect.x > player2Rect.x:
            if counter_pillager_axe_p1 % 60 < 20:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe1.png"),
                                                     (92 * 4, 134 * 3.5))
            elif counter_pillager_axe_p1 % 60 < 40:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe2.png"),
                                                     (92 * 4, 134 * 3.5))
            elif counter_pillager_axe_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe3.png"),
                                                     (92 * 4, 134 * 3.5))

        else:
            if counter_pillager_axe_p1 % 60 < 20:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe1.png"),
                                           (92 * 4, 134 * 3.5)), True, False)
            elif counter_pillager_axe_p1 % 60 < 40:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe2.png"),
                                           (92 * 4, 134 * 3.5)), True, False)
            elif counter_pillager_axe_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe3.png"),
                                           (92 * 4, 134 * 3.5)), True, False)
    if pillager_cr_p1:
        counter_pillager_cr_p1 += 10
        if player1Rect.x > player2Rect.x:
            if counter_pillager_cr_p1 % 60 < 15:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow1.png"),
                                                     (104 * 3.5, 134 * 3.5))
            elif counter_pillager_cr_p1 % 60 < 30:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow2.png"),
                                                     (104 * 3.5, 134 * 3.5))
            elif counter_pillager_cr_p1 % 60 < 45:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow3.png"),
                                                     (104 * 3.5, 134 * 3.5))
            elif counter_pillager_cr_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow4.png"),
                                                     (104 * 3.5, 134 * 3.5))
        else:
            if counter_pillager_cr_p1 % 60 < 15:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow1.png"),
                                           (104 * 3.5, 134 * 3.5)), True, False)
            elif counter_pillager_cr_p1 % 60 < 30:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow2.png"),
                                           (104 * 3.5, 134 * 3.5)), True, False)
            elif counter_pillager_cr_p1 % 60 < 45:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow3.png"),
                                           (104 * 3.5, 134 * 3.5)), True, False)
            elif counter_pillager_cr_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow4.png"),
                                           (104 * 3.5, 134 * 3.5)), True, False)
    if ravager_p1:
        counter_ravager_p1 += 12
        if player1Rect.x > player2Rect.x:
            if counter_ravager_p1 % 60 < 20:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_header1.png"),
                                                     (172 * 6, 84 * 6))
            elif counter_ravager_p1 % 60 < 40:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_header2.png"),
                                                     (172 * 6, 84 * 6))
            elif counter_ravager_p1 % 60 < 59:
                player1Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_header3.png"),
                                                     (172 * 6, 84 * 6))

        else:
            if counter_ravager_p1 % 60 < 20:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_header1.png"),
                                           (172 * 6, 84 * 6)), True, False)
            elif counter_ravager_p1 % 60 < 40:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_header2.png"),
                                           (172 * 6, 84 * 6)), True, False)
            elif counter_ravager_p1 % 60 < 59:
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_header3.png"),
                                           (172 * 6, 84 * 6)), True, False)

    # ==================================Animation Player 2========================================
    if ghast_header_p2:
        counter_ghast_header_p2+=12
        if player2Rect.y==250:
            player2Rect.y = 50
        else:
            player2Rect.y+=50
        if player1Rect.x>player2Rect.x:
            if counter_ghast_header_p2%60<12:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header1.png"), (212 * 4, 208 * 4))
            elif counter_ghast_header_p2%60<24:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header2.png"), (212 * 4, 208 * 4))
            elif counter_ghast_header_p2%60<36:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header3.png"), (212 * 4, 208 * 4))
            elif counter_ghast_header_p2%60<48:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header4.png"), (212 * 4, 208 * 4))
            elif counter_ghast_header_p2%60<59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_header5.png"), (212 * 4, 208 * 4))
            health_player1 -= 2
        else:
            if counter_ghast_header_p2%60<12:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_header1.png"), (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p2%60<24:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_header2.png"), (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p2%60<36:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_header3.png"), (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p2%60<48:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_header4.png"), (212 * 4, 208 * 4)), True, False)
            elif counter_ghast_header_p2%60<59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_header5.png"), (212 * 4, 208 * 4)), True, False)
            health_player1 -= 2
    print(ghast_snow_p2)
    if ghast_snow_p2:
        counter_ghast_snow_p2+=12
        if player1Rect.x>player2Rect.x:
            if counter_ghast_snow_p2%60<30:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_snow1.png"), (108 * 4.5, 112 * 4.5))
            elif counter_ghast_snow_p2%60<59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_snow2.png"), (108 * 4.5, 112 * 4.5))
        else:
            if counter_ghast_snow_p2 % 60 < 30:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_snow1.png"),
                                                                           (108 * 4.5, 112 * 4.5)),True,False)
            elif counter_ghast_snow_p2 % 60 < 59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_snow2.png"),
                                                                           (108 * 4.5, 112 * 4.5)),True,False)
    if ghast_laser_p2:
        counter_ghast_laser_p2+=10

        if player1Rect.x>player2Rect.x:
            if counter_ghast_laser_p2%60<15:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser1.png"), (108 * 4.5, 112 * 4.5))
            elif counter_ghast_laser_p2%60<30:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser2.png"), (108 * 4.5, 112 * 4.5))
            elif counter_ghast_laser_p2%60<45:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser2.png"), (108 * 4.5, 112 * 4.5))
            elif counter_ghast_laser_p2%60<59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/ghast_laser4.png"), (108 * 4.5, 112 * 4.5))
        else:
            if counter_ghast_laser_p2%60<15:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_laser1.png"), (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_laser_p2%60<30:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_laser2.png"), (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_laser_p2%60<45:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_laser2.png"), (108 * 4.5, 112 * 4.5)), True, False)
            elif counter_ghast_laser_p2%60<59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/ghast_laser4.png"), (108 * 4.5, 112 * 4.5)), True, False)
    if blaze_hit_p2:
        counter_blaze_hit_p2 += 12
        if player1Rect.x < player2Rect.x:
            print(1)
            if counter_blaze_hit_p2 % 60 < 20:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit1.png"),
                                                     (136 * 4, 116 * 4))
            elif counter_blaze_hit_p2 % 60 < 40:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit2.png"),
                                                     (136 * 4, 116 * 4))
            elif counter_blaze_hit_p2 % 60 < 59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_hit3.png"),
                                                     (136 * 4, 116 * 4))

            health_player1 -= 2
        else:
            print(2)
            if counter_blaze_hit_p2 % 60 < 20:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_hit1.png"),
                                                                           (136 * 4, 116 * 4)), True, False)
            elif counter_blaze_hit_p2 % 60 < 40:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_hit2.png"),
                                                                           (136 * 4, 116 * 4)), True, False)
            elif counter_blaze_hit_p2 % 60 < 59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_hit3.png"),
                                                                           (136 * 4, 116 * 4)), True, False)
    if blaze_throw_p2:
        counter_blaze_throw_p2+=12
        rods_rect2.y= player2Rect.y+100
        if player1Rect.x<player2Rect.x:
            print(1)
            if counter_blaze_throw_p2%60<12:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"), (82 * 4, 128 * 4))
            elif counter_blaze_throw_p2%60<24:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"), (82 * 4, 128 * 4))
            elif counter_blaze_throw_p2%60<36:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"), (82 * 4, 128 * 4))
            elif counter_blaze_throw_p2%60<48:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"), (82 * 4, 128 * 4))
            elif counter_blaze_throw_p2%60<59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"), (82 * 4, 128 * 4))
            health_player1 -= 2
        else:
            print(2)
            if counter_blaze_throw_p2%60<12:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_throw_rods1.png"), (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p2%60<24:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_throw_rods2.png"), (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p2%60<36:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_throw_rods3.png"), (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p2%60<48:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_throw_rods4.png"), (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_p2%60<59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/blaze_throw_rods5.png"), (82 * 4, 128 * 4)), True, False)
    if blaze_throw_all_p2:
        counter_blaze_throw_all_p2 += 12
        rods_rect.y = player2Rect.y + 100
        if player1Rect.x < player2Rect.x:
            print(1)
            if counter_blaze_throw_all_p2 % 60 < 12:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p2 % 60 < 24:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p2 % 60 < 36:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p2 % 60 < 48:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"),
                                                     (82 * 4, 128 * 4))
            elif counter_blaze_throw_all_p2 % 60 < 59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"),
                                                     (82 * 4, 128 * 4))
            health_player1 -= 2
        else:
            print(2)
            if counter_blaze_throw_all_p2 % 60 < 12:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods1.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p2 % 60 < 24:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods2.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p2 % 60 < 36:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods3.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p2 % 60 < 48:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods4.png"),
                                           (82 * 4, 128 * 4)), True, False)
            elif counter_blaze_throw_all_p2 % 60 < 59:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/blaze_throw_rods5.png"),
                                           (82 * 4, 128 * 4)), True, False)

    if pillager_axe_p2:
        counter_pillager_axe_p2 += 12
        if player1Rect.x < player2Rect.x:
            print(1)
            if counter_pillager_axe_p2 % 60 < 20:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe1.png"),
                                                     (92 * 4, 134 * 3.5))
            elif counter_pillager_axe_p2 % 60 < 40:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe2.png"),
                                                     (92 * 4, 134 * 3.5))
            elif counter_pillager_axe_p2 % 60 < 59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_axe3.png"),
                                                     (92 * 4, 134 * 3.5))

        else:
            print(2)
            if counter_pillager_axe_p2 % 60 < 20:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/pillager_axe1.png"),
                                                                           (92 * 4, 134 * 3.5)), True, False)
            elif counter_pillager_axe_p2 % 60 < 40:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/pillager_axe2.png"),
                                                                           (92 * 4, 134 * 3.5)), True, False)
            elif counter_blaze_hit_p2 % 60 < 59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/pillager_axe3.png"),
                                                                           (92 * 4, 134 * 3.5)), True, False)
    if pillager_cr_p2:
        counter_pillager_cr_p2 += 10
        if player1Rect.x < player2Rect.x:
            if counter_pillager_cr_p2 % 60 < 15:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow1.png"),
                                                     (104 *3.5, 134 * 3.5))
            elif counter_pillager_cr_p2 % 60 < 30:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow2.png"),
                                                     (104 *3.5, 134 * 3.5))
            elif counter_pillager_cr_p2 % 60 < 45:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow3.png"),
                                                     (104 *3.5, 134 * 3.5))
            elif counter_pillager_cr_p2 % 60 < 59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow4.png"),
                                                     (104 *3.5, 134 * 3.5))
        else:
            if counter_pillager_cr_p2 % 60 < 15:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow1.png"),
                                           (104 *3.5, 134 * 3.5)), True, False)
            elif counter_pillager_cr_p2 % 60 < 30:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow2.png"),
                                           (104 *3.5, 134 * 3.5)), True, False)
            elif counter_pillager_cr_p2 % 60 < 45:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow3.png"),
                                           (104 *3.5, 134 * 3.5)), True, False)
            elif counter_pillager_cr_p2 % 60 < 59:
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/animation/pillager_crossbow4.png"),
                                           (104 *3.5, 134 * 3.5)), True, False)
    if ravager_p2:
        counter_ravager_p2 += 12
        if player1Rect.x < player2Rect.x:
            print(1)
            if counter_ravager_p2 % 60 < 20:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_header1.png"),
                                                     (172 * 6, 84*6))
            elif counter_ravager_p2 % 60 < 40:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_header2.png"),
                                                     (172 * 6, 84*6))
            elif counter_ravager_p2 % 60 < 59:
                player2Surf = pygame.transform.scale(pygame.image.load("assets/animation/pillager_header3.png"),
                                                     (172 * 6, 84*6))

        else:
            print(2)
            if counter_ravager_p2 % 60 < 20:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/pillager_header1.png"),
                                                                           (172 * 6, 84*6)), True, False)
            elif counter_ravager_p2 % 60 < 40:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/pillager_header2.png"),
                                                                           (172 * 6, 84*6)), True, False)
            elif counter_ravager_p2 % 60 < 59:
                player2Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/animation/pillager_header3.png"),
                                                                           (172 * 6, 84*6)), True, False)
    if prev_health_p1 > health_player1:
        if player1Rect.x > player2Rect.x:
            if player1 =="1":
                player1Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/Happy_Ghast_hurts.png").convert_alpha(),
                                           (108 * 4.5, 112 * 4.5)), True, False)

            if player1=='2':
                player1Surf = pygame.transform.scale(pygame.image.load("assets/Blaze_hurts.png").convert_alpha(),
                                                     (164 * 2, 232 * 2))

            if player1=='3':
                player1Surf = pygame.transform.scale(pygame.image.load("assets/Pillager_hurts.png").convert_alpha(),
                                                     (148 * 2, 238 * 2))
        else:
            if player1 =="1":
                player1Surf = pygame.transform.scale(pygame.image.load("assets/Happy_Ghast_hurts.png").convert_alpha(),
                                                     (108 * 4.5, 112 * 4.5))
            if player1=='2':
                player1Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/Blaze_hurts.png").convert_alpha(),
                                                                           (164 * 2, 232 * 2)),True,False)

            if player1=='3':
                player1Surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                    "assets/Pillager_hurts.png").convert_alpha(),
                                                                           (148 * 2, 238 * 2)),True,False)
    if prev_health_p2 > health_player2:
        print("exec")
        if player1Rect.x < player2Rect.x:
            if player2 == "1":
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/Happy_Ghast_hurts.png").convert_alpha(),
                                           (108 * 4.5, 112 * 4.5)), True, False)

            if player2 == '2':
                player2Surf = pygame.transform.scale(pygame.image.load("assets/Blaze_hurts.png").convert_alpha(),
                                                     (164 * 2, 232 * 2))

            if player2 == '3':
                player2Surf = pygame.transform.scale(pygame.image.load("assets/Pillager_hurts.png").convert_alpha(),
                                                     (148 * 2, 238 * 2))
        else:
            if player2 == "1":
                player2Surf = pygame.transform.scale(
                    pygame.image.load("assets/Happy_Ghast_hurts.png").convert_alpha(),
                    (108 * 4.5, 112 * 4.5))
            if player2 == '2':

                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/Blaze_hurts.png").convert_alpha(),
                                           (164 * 2, 232 * 2)), True, False)

            if player2 == '3':
                print("got exec")
                player2Surf = pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("assets/Pillager_hurts.png").convert_alpha(),
                                           (148 * 2, 238 * 2)), True, False)
    if crouched_p1:
        if player1 == '1':
            player1Rect.y+=200
        if player1 == '2':
            player1Rect.y+=200

        if player1 == '3':
            player1Rect.y+=200
    if crouched_p2:

        if player2 == '1':
            player2Rect.y+=200
        if player2 == '2':
            player2Rect.y+=200

        if player2 == '3':
            player2Rect.y+=200

    screen.blit(player1Surf,player1Rect)
    screen.blit(player2Surf,player2Rect)

    if health_player1 <=0:
        health_player1-=555
        if health_player1 >-600:
            screen.blit(ko_surf,ko_rect)
            pygame.display.update()
            pygame.time.delay(700)
        screen.blit(background_surf, background_rect)
        screen.blit(victoryp2_surf, victoryp2_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(quit_surf, quit_rect)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_rect.collidepoint(event.pos):
                    sys.exit()
                elif restart_rect.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(['python','fullGame.py'])

                    sys.exit()
                break

    if health_player2<=0:
        health_player2 -=555
        if health_player2 > -600:
            screen.blit(ko_surf, ko_rect)
            pygame.display.update()
            pygame.time.delay(700)



        screen.blit(background_surf, background_rect)
        screen.blit(victoryp1_surf, victoryp1_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(quit_surf, quit_rect)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_rect.collidepoint(event.pos):
                    sys.exit()
                elif restart_rect.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(['python', 'fullGame.py'])
                    sys.exit()

    prev_health_p1 = health_player1
    prev_health_p2 = health_player2
    pygame.display.flip()
    clock.tick(60)#Ceiling FPS
