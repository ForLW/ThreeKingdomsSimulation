class General:
    def __init__(self, name, force, blood_top, blood, skill):
        """
        # 武将构造函数
        :param name: 武将名
        :param force: 武将所属势力
        :param blood_top: 武将体力上限
        :param blood: 武将当前体力值
        :param skill: 武将技能
        """
        self.blood_top = blood_top
        self.blood = blood
        self.force = force
        self.name = name
        self.skill = skill

    def show(self):
        print("武将名：{}".format(self.name))
        print("势力：{}".format(self.force))
        print("体力上限：{}".format(self.blood_top))
        print("当前体力值：{}".format(self.blood))
        print("技能：{}".format(self.skill))
        # for i in self.skill:
        #     print("{}：{}".format(i, self.skill[i]))

    def get_name(self):
        return self.name

    def get_force(self):
        return self.force

    def get_blood(self):
        return self.blood

    def get_blood_top(self):
        return self.blood_top

    def get_skill_name(self):
        pass

    def modify_blood(self, num):
        self.blood += num

    def modify_blood_top(self, num):
        self.blood_top += num

