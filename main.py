import os
import time

from general import General
from card import *
from player import Player
import player
import random

generalList = []
cardList = []


def mainInit():
    g = General("关羽", "蜀", 4, 4, {"武圣": "可以把红色牌当杀"})
    generalList.append(g)
    g = General("张飞", "蜀", 4, 4, {"咆哮": "无限出杀"})
    generalList.append(g)
    g = General("赵云", "蜀", 4, 4, {"龙胆": "杀当闪,闪当杀"})
    generalList.append(g)

    # A
    c = Card("A", "黑桃", "决斗", "非延时锦囊牌")
    cardList.append(c)
    c = Card("A", "黑桃", "闪电", "延时锦囊牌")
    cardList.append(c)
    c = Card("A", "黑桃", "古锭刀(2)", "武器牌")
    cardList.append(c)

    c = Card("A", "红桃", "万箭齐发", "非延时锦囊牌")
    cardList.append(c)
    c = Card("A", "红桃", "桃园结义", "非延时锦囊牌")
    cardList.append(c)
    c = Card("A", "红桃", "无懈可击", "非延时锦囊牌")
    cardList.append(c)

    c = Card("A", "草花", "决斗", "非延时锦囊牌")
    cardList.append(c)
    c = Card("A", "草花", "诸葛连弩(1)", "武器牌")
    cardList.append(c)
    c = Card("A", "草花", "白银狮子", "防具牌")
    cardList.append(c)

    c = Card("A", "方片", "决斗", "非延时锦囊牌")
    cardList.append(c)
    c = Card("A", "方片", "诸葛连弩(1)", "武器牌")
    cardList.append(c)
    c = Card("A", "方片", "朱雀羽扇(4)", "武器牌")
    cardList.append(c)

    # 2
    c = Card("2", "黑桃", "八卦阵", "防具牌")
    cardList.append(c)
    c = Card("2", "黑桃", "雌雄双股剑", "武器牌")
    cardList.append(c)
    c = Card("2", "黑桃", "藤甲", "防具牌")
    cardList.append(c)
    c = Card("2", "黑桃", "寒冰箭(2)", "武器牌")
    cardList.append(c)

    c = Card("2", "红桃", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "红桃", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "红桃", "火攻", "非延时锦囊牌")
    cardList.append(c)

    c = Card("2", "草花", "杀", "非延时锦囊牌")
    cardList.append(c)
    c = Card("2", "草花", "八卦阵", "防具牌")
    cardList.append(c)
    c = Card("2", "草花", "藤甲", "防具牌")
    cardList.append(c)
    c = Card("2", "草花", "仁王盾", "防具牌")
    cardList.append(c)

    c = Card("2", "方片", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "方片", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "方片", "桃", "基本牌")
    cardList.append(c)

    # 3
    c = Card("3", "黑桃", "八卦阵", "防具牌")
    cardList.append(c)
    c = Card("2", "黑桃", "雌雄双股剑", "武器牌")
    cardList.append(c)
    c = Card("2", "黑桃", "藤甲", "防具牌")
    cardList.append(c)
    c = Card("2", "黑桃", "寒冰箭(2)", "武器牌")
    cardList.append(c)

    c = Card("2", "红桃", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "红桃", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "红桃", "火攻", "非延时锦囊牌")
    cardList.append(c)

    c = Card("2", "草花", "杀", "非延时锦囊牌")
    cardList.append(c)
    c = Card("2", "草花", "八卦阵", "防具牌")
    cardList.append(c)
    c = Card("2", "草花", "藤甲", "防具牌")
    cardList.append(c)
    c = Card("2", "草花", "仁王盾", "防具牌")
    cardList.append(c)

    c = Card("2", "方片", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "方片", "闪", "基本牌")
    cardList.append(c)
    c = Card("2", "方片", "桃", "基本牌")
    cardList.append(c)


# # 提示内容
# def show_tips(text, count):
#     os.system("cls")
#     print(text, end="")
#     for i in range(count):
#         time.sleep(0.5)
#         print(".", end="")
#     print()


# 洗牌
def clean_card():
    # 洗牌
    for i in range(len(cardList)):
        idx = random.randint(0, len(cardList) - 1)
        temp = cardList.pop(idx)
        idx = random.randint(0, len(cardList) - 2)
        cardList.insert(idx, temp)


if __name__ == '__main__':
    # 卡牌初始化
    mainInit()

    # 提示内容
    player.show_tips("正在洗牌", 4)

    # 洗牌
    clean_card()
    player1 = Player("张三",
                     generalList.pop(random.randint(0, len(generalList) - 1)))
    player2 = Player("李四",
                     generalList.pop(random.randint(0, len(generalList) - 1)))
    # 显示玩家信息
    print("-" * 20)
    player1.show()
    print("-" * 20)
    player2.show()
    print("-" * 20)

    player.show_tips("玩家发牌", 4)
    # 开局发牌
    player1.touch_card_up(cardList, 4)
    player2.touch_card_up(cardList, 4)
    print("-" * 20)
    player1.show_card()
    print("-" * 20)
    player2.show_card()
    print("-" * 20)

    # 随机第一回合玩家
    coin = random.randint(1, 2)

    while True:
        if coin == 1:
            # 玩家一
            player1.game_flow(cardList)
            coin = 2
        elif coin == 2:
            # 玩家二
            player2.game_flow(cardList)
            coin = 1
