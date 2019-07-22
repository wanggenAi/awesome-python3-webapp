class Game(object):

    # 历史最高分
    top_score = 0
    def __init__(self,play_name):
        self.player_name = play_name

    @staticmethod
    def show_help():
        print("这个游戏没法玩")

    @classmethod
    def show_top_score(cls):
        print("历史记录：%d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)

Game.show_help()
Game.show_top_score()
wg_game = Game("王根")
wg_game.start_game()