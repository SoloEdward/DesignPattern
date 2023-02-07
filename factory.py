class Hero(object):
    
    def move(self):
        return "Move It"

    def skillA(self):
        raise NotImplementedError()

    def skillB(self):
        raise NotImplementedError()

    @staticmethod
    def factory(hero_name):
        return {'ZhuangZhou': ZhuangZhou(), 'ZhongWuYan': ZhongWuYan()}[hero_name]

class ZhuangZhou(Hero):
    def skillA(self):
        return 'skillA of ZhuangZhou'

    def skillB(self):
        return 'skillB of ZhuangZhou'

class ZhongWuYan(Hero):
    def skillA(self):
        return 'skillA of ZhongWuYan'

    def skillB(self):
        return 'skillB of ZhongWuYan'

if __name__ == '__main__':
    hero = Hero.factory('ZhuangZhou')
    print(hero.skillA())
    print(hero.skillB())
    print(hero.move())
