import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 设置定时器事件 创建敌机、发射子弹
        pygame.time.set_timer(CREATE_ENEMY_EVENT,300)
        pygame.time.set_timer(HERO_FIRE_EVENT,200)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


        pass

    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()


    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 使用键盘按键来获取
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = SPEED_HERO
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -SPEED_HERO
            else:
                self.hero.speed = 0




    def __check_collide(self):
        # 子弹和敌机碰撞
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies):
            self.hero.kill()
            PlaneGame.__game_over()
            print("游戏结束")

    def __update_sprites(self):
        # 更新背景精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 更新敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 更新英雄子弹精灵组
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    pg = PlaneGame()
    pg.start_game()