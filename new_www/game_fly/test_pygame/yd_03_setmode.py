import pygame
from  plane_sprites import  *
# 创建屏幕
pygame.init()

screen = pygame.display.set_mode((480,700))

# 加载背景图片
bg = pygame.image.load("../images/background.png")
screen.blit(bg,(0,0))
# pygame.display.update()

# 英雄飞机
hero = pygame.image.load("../images/me1.png")
screen.blit(hero,(200,500))

# 可以在所有绘制工作完成后统一调用
pygame.display.update()


# 游戏时钟,可以控制程序运行的时间 控制帧数
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200,500,102,126)

# 创建敌机的精灵
enemy = GameSprite("../images/enemy1.png")
enemy1 = GameSprite("../images/enemy1.png",2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

# 游戏循环 -> 意味着游戏的正式开始！
while True:
    clock.tick(60)


    for event in pygame.event.get():

        # 判断时间是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出")
            exit()

    # 2. 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y == -126:
        hero_rect.y = 700

    # 3. 重新绘制英雄图片
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    # 精灵组调用两个方法update draw
    enemy_group.update()
    enemy_group.draw(screen)


    # 4. 重新加载屏幕
    pygame.display.update()
pygame.quit()







