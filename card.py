class Card:
    def __init__(self, count, flower, name, type_name):
        self.count = count
        self.flower = flower
        self.name = name
        self.type_name = type_name

    def show(self):
        print("点数:{} 花色:{} 名称:{} 类型:{}".format(self.count, self.flower, self.name, self.type_name))


def card_count_complete(card1, card2):
    count_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "10": 10, "J": 11, "Q": 12, "K": 13}
    if count_dict[card1.count] >= count_dict[card2.count]:
        return True
    else:
        return False
