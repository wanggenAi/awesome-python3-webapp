import pygame

hero_rect = pygame.Rect(100,500,120,125)
print("远点：%d %d" % (hero_rect.x,hero_rect.y))
print("尺寸 %d %d" % (hero_rect.width,hero_rect.height))
print("元组尺寸：%d %d" % hero_rect.size)

