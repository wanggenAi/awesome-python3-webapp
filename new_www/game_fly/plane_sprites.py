import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄的按键速度
SPEED_HERO = 5
# 英雄发射子弹的事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self,image_name,speed=1):
        # 调用父类的方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向上移动，正数向下，负数向上
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt = False):
        # 调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        # 判断是否是交替图像，如果是需要设置初始位置
        if is_alt:
           self.rect.y = -self.rect.height

    def update(self):
        # 1. 调用父类的方法实现
        super().update()
        # 2. 如果移出屏幕则将图像移动到屏幕上方
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2. 指定敌机初始随机速度 1~3
        self.speed = random.randint(1, 3)
        # 3. 初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)

    def update(self):
        # 1. 调用父类方法保持垂直方向飞行
        super().update()
        # 2. 判断是否飞出屏幕，如果是则需要从精灵组删除敌机
        if self.rect.y > SCREEN_RECT.height:
            # 可以将精灵从所有精灵组移出，并销毁这个精灵对象。__del__内置方法可以捕获到哦
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1. 调用父类方法设置image和speed
        super().__init__("./images/me1.png",0)
        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.bottom - 180
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹")
        for i in (0,1,2):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置初始位置英雄正上方
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 添加到英雄子弹精灵组
            self.bullets.add(bullet)



class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法图片速度
        super().__init__("./images/bullet1.png", -5)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()
