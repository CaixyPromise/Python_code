# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

import random
import re
import time

use_num = dict()  # 人数编号字典
final_name = list()  # 人员名单列表
count_num = 0

def random_funcA(count ,peoNum):
    global count_num
    for i in range(1,count+1):  # 生成编号字典
        use_num[i] = 0

    while True:
        count_num += 1
        if peoNum == len(final_name):
            break
        choice_num = random.randint(1,count)

        if str(choice_num) in final_name:
            continue
        final_name.append(str(choice_num))

    return f"随机结果:"+" ".join(final_name)

def random_funcB(count , peoNum , loop):
    global count_num
    for i in range(1,count+1):  # 生成编号字典
        use_num[i] = 0

    while True:
        count_num += 1
        if peoNum == len(final_name):
            break
        choice_num = random.randint(1,count)

        if use_num[choice_num] != loop:
            use_num[choice_num] += 1

        elif use_num[choice_num] == loop:
            if str(choice_num) in final_name:
                continue
            final_name.append(str(choice_num))

    return f"随机结果:"+" ".join(final_name)

def menu():
    # 菜单
    print("""
    ☆☆☆☆☆——————————————WELCOME TO RANDOM. SYSTEM————————————————————☆☆☆☆☆
                       ===========功能菜单===========
                            ◎1.随机摇号>>>单次摇号模式
                            ◎2.随机摇号>>>多次摇号模式
                            ◎0.退出关闭
                     程序测试阶段  如有BUG或建议请联系作者  
                       =============================
    ☆☆☆☆☆————————————————————没有感情的分界线————————————————————————☆☆☆☆☆
    """)

def main():
    condition = True
    while condition:
        menu()
        option = input("请选择功能：")
        option_str = re.sub(r'\D', "", option)
        if option_str in ['0', '1', '2','3','4','5','6','7','8']:
            option_int = int(option_str)
            if option_int == 0:
                sum = 3  # 设置倒计时时间
                timeflush = 0.25  # 设置屏幕刷新的间隔时间
                for i in range(0, int(sum / timeflush)):
                    list = ["\\", "|", "/", "—"]
                    index = i % 4
                    print("\r您已成功退出，正在关闭中！欢迎再次使用，再见 {}".format(list[index]), end="")
                    time.sleep(timeflush)
                condition = False
                exit()
            elif option_int == 1:
                put_count = int(input("参与人数:"))
                put_peoNu = int(input("摇号人数:"))
                print(random_funcA(put_count,put_peoNu))
            elif option_int == 2:
                put_count = int(input("参与人数:"))
                put_peoNu = int(input("摇号人数:"))
                put_Nloop = int(input("循环次数:"))
                print(random_funcB(put_count,put_peoNu,put_Nloop))

if __name__ == '__main__':
    main()
