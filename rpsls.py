#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张跃荣
日期：2021/11/28
"""

import random





# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    else:
        return 4






def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "纸"
    elif number==3:
        return "蜥蜴"
    else:
        return "剪刀"



def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("----------------")
    print("您的选择为%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    computer_result=number_to_name(comp_number)
    print("计算机的选择为：%s"%computer_result)
    num=player_choice_number-comp_number
    if num==1 or num==2 or num==-3 or num==-4:
        print("您赢了")
    elif num==0:
        print ("您和计算机出的一样呢")
    else:
        print("计算机赢了")
"""
规则为：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克；史波克打碎剪刀；剪刀腰斩蜥蜴；蜥蜴吃掉布；纸反驳史波克；史波克蒸发石头
若用户赢，有以下10种情况：(玩家-计算机）
相减为一：4-3,3-2,2-1，1-0
相减为二：4-2,3-1,2-0
相减为-3:0-3,1-4
相减为-4:0-4
如果相减为零则显示“您和计算机出的一样”
反之计算机赢得游戏
"""




# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


