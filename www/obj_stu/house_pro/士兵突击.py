class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count < 0:
            print("子弹不够了，请上弹")
            return
        self.bullet_count-=1
        print("%s 射了一发子弹！还剩 %d 发" % (self.model,self.bullet_count))


class Soldier:
    def __init__(self,name):
        self.name = name
        #  新兵没有枪
        self.gun = None

    def fire(self):
        pass

ak47 = Gun("AK47")
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun.model)


