import os
import time


class Player:
    def __init__(self, name, general):
        """
        :param name: 玩家名
        :param general: 武将
        """
        self.id = name
        self.general = general
        self.identity = ""
        self.plate = []
        self.paddock = {"武器": "", "防具": "", "防御马": "", "进攻马": ""}
        self.determine_the_area = ""
        self.kill_count = 1
        self.is_drink_wine = 0

    def show(self):
        print("玩家名:{}".format(self.id))
        self.general.show()
        print("装备区:{}".format(self.paddock))
        print("判定区:{}".format(self.determine_the_area))

    def show_card(self):
        print("{}手牌:".format(self.general.get_name()))
        for i in range(1, len(self.plate) + 1):
            print("{}:".format(i), end="")
            self.plate[i - 1].show()

    def touch_card_up(self, cardList, count):
        """
        玩家摸牌功能
        :param cardList: 牌堆列表
        :param count: 摸牌数量
        :return: 牌堆列表
        """
        for i in range(count):
            if len(cardList) != 0:
                self.plate.append(cardList.pop(0))
            else:
                pass
                # 重新洗牌
        return cardList

    def get_plate_len(self):
        return len(self.plate)

    def game_flow(self, cardList):
        # 获取武将信息
        general_name = self.general.get_name()

        # 回合开始阶段
        print("-" * 20)
        print("{}回合开始阶段".format(general_name))
        show_tips("", 4)

        # 判定阶段
        print("-" * 20)
        print("{}判定阶段".format(general_name))
        show_tips("", 4)
        if self.determine_the_area != "":
            # 进行判定
            print("")

        # 摸牌阶段
        print("-" * 20)
        print("{}摸牌阶段".format(general_name))
        show_tips("", 4)
        self.touch_card_up(cardList, 2)

        # 出牌开始
        print("-" * 20)
        print("{}出牌开始阶段".format(general_name))
        show_tips("", 4)

        # 出牌阶段

        # 默认设置可出杀次数为1
        self.kill_count = 1
        # 默认设置喝酒状态为0
        self.is_drink_wine = 0
        while True:
            print("-" * 20)
            print("{}出牌阶段".format(general_name))
            print("-" * 20)
            self.show_card()
            print("-" * 20)
            idx = input("请选择要出的牌序号(输入结束出牌结束):")
            # 输入结束
            if idx == "结束":
                break
            # 正常出牌
            else:
                # 判断输入内容是否为数字
                try:
                    idx = int(idx)
                except Exception as ex:
                    print("输入的内容不对啊:{}".format(ex))
                else:
                    # 判断是否有输入的手牌
                    if idx > self.get_plate_len():
                        print("没有那张牌哦")
                    else:
                        # 卡牌类型
                        type_name = self.plate[idx - 1].type_name
                        card_name = self.plate[idx - 1].name
                        # 基本牌
                        if type_name == "基本牌":
                            # 出杀
                            if "杀" in list(card_name):
                                if self.kill_count > 0:
                                    # 选择杀的目标
                                    pass
                                    # 判断攻击距离
                                    print("{}出牌:".format(general_name))
                                    card = self.plate.pop(idx - 1)
                                    card.show()
                                    # 被杀玩家响应
                                    pass
                                else:
                                    print("不能再出杀了")
                            # 出桃
                            elif "桃" == card_name:
                                if self.general.get_blood() < self.general.get_blood_top():
                                    print("{}出牌:".format(general_name))
                                    card = self.plate.pop(idx - 1)
                                    self.general.modify_blood(1)
                                    card.show()
                                else:
                                    print("满血不能吃桃")
                            elif "酒" == card_name:
                                if self.is_drink_wine == 0:
                                    print("{}出牌:".format(general_name))
                                    card = self.plate.pop(idx - 1)
                                    self.is_drink_wine = 1
                                    card.show()
                                else:
                                    print("不能再喝了要喝多了")
                        # 非延时锦囊牌
                        elif type_name == "非延时锦囊牌" and card_name != "无懈可击":
                            # 决斗
                            # 顺手牵羊
                            # 过河拆桥
                            # 万箭齐发
                            # 南蛮入侵
                            # 五谷丰登
                            # 桃园结义
                            # 借刀杀人
                            # 火攻
                            pass
                        # 延时锦囊牌
                        elif type_name == "延时锦囊牌":
                            # 乐不思蜀
                            # 兵粮寸断
                            # 闪电
                            pass
                        # 武器牌
                        elif type_name == "武器牌":
                            self.paddock["武器"] = self.plate.pop(idx)
                            print("装备武器:{}".format(self.paddock["武器"]))
                        # 防具牌
                        elif type_name == "防具牌":
                            self.paddock["防具"] = self.plate.pop(idx)
                            print("装备武器:{}".format(self.paddock["防具"]))
                        # 进攻马
                        elif type_name == "进攻马":
                            self.paddock["进攻马"] = self.plate.pop(idx)
                            print("装备武器:{}".format(self.paddock["进攻马"]))
                        # 防御马
                        elif type_name == "防御马":
                            self.paddock["防御马"] = self.plate.pop(idx)
                            print("装备武器:{}".format(self.paddock["防御马"]))

        # 出牌结束
        print("-" * 20)
        print("{}结束出牌".format(general_name))
        show_tips("", 4)

        # 弃牌阶段
        print("-" * 20)
        print("{}弃牌阶段".format(general_name))
        show_tips("", 4)
        plate_len = self.get_plate_len()
        blood = self.general.get_blood()
        if plate_len > blood:
            print("请弃置{}张牌".format(plate_len - blood))
            while plate_len > blood:
                try:
                    idx = int(input("选择要弃牌第几张牌:"))
                except Exception as ex:
                    print("请输入数字{}".format(ex))
                else:
                    try:
                        self.plate.pop(idx - 1)
                    except Exception as ex:
                        print("没有这张牌:{}".format(ex))
                    else:
                        self.show_card()
                        plate_len = self.get_plate_len()
                        blood = self.general.get_blood()

        # 回合结束阶段
        print("-" * 20)
        print("{}回合结束阶段".format(general_name))
        show_tips("", 4)


# 提示内容
def show_tips(text="", count=4):
    # os.system("cls")
    print(text, end="", flush=True)
    for i in range(count):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    os.system("cls")
