#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���Ծ��
���ڣ�2021/11/28
"""

import random





# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    else:
        return 4






def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    else:
        return "����"



def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("----------------")
    print("����ѡ��Ϊ%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    computer_result=number_to_name(comp_number)
    print("�������ѡ��Ϊ��%s"%computer_result)
    num=player_choice_number-comp_number
    if num==1 or num==2 or num==-3 or num==-4:
        print("��Ӯ��")
    elif num==0:
        print ("���ͼ��������һ����")
    else:
        print("�����Ӯ��")
"""
����Ϊ�������ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ���ˣ�ʷ���˴��������������ն���棻����Ե�����ֽ����ʷ���ˣ�ʷ��������ʯͷ
���û�Ӯ��������10�������(���-�������
���Ϊһ��4-3,3-2,2-1��1-0
���Ϊ����4-2,3-1,2-0
���Ϊ-3:0-3,1-4
���Ϊ-4:0-4
������Ϊ������ʾ�����ͼ��������һ����
��֮�����Ӯ����Ϸ
"""




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


