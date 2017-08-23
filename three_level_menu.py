#!/usr/bin/env python3
# Author: Yingqin He

import json
import os


def load_file():
    # 加载本地json文件
    with open('product_list.json') as f:
        product_list = json.load(f)
    return product_list

current_menu = load_file()
menus = [current_menu]

color_red = '\033[1;31m'  # 红色加粗字体，用于显示错误类提示信息
color_yellow = '\033[1;33m'  # 黄色加粗字体，用于显示菜单
color_green = '\033[1;32m'  # 绿色加粗字体，用于显示成功类提示信息
color_end = '\033[0m'  # 颜色结束符

while True:
    os.system('clear')  # 显示菜单前进行清屏
    item = 'init'  # 定义一个变量item，如果不定义的话，程序也能正常运行，但是不符合规范
    index_item = {}  # 定义一个空字典，用于保存enumerate()生成的索引和current_menu的键值的对应关系
    print('%s+++++++++++++++' % color_yellow)
    for index, item in enumerate(current_menu, 1):
        if isinstance(current_menu[item], dict):
            print(index, item)  # 如果菜单不是最后一级，就显示index及key
        else:
            print(index, item, current_menu[item])  # 如果菜单是最后一级，就显示index、key及value
        index_item[str(index)] = item  # 保存enumerate()生成的索引和current_menu的键值的对应关系
    print('+++++++++++++++%s' % color_end)

    if len(menus) == 1:  # 如果菜单是第一级，只能进入下级菜单或退出
        user_choice = input('输入相应数字进入下级菜单，或输入"q"退出：').strip()
        while True:
            if user_choice.lower() == 'q':
                exit('%s感谢您的使用！%s' % (color_green, color_end))
            elif user_choice in index_item:
                menus.append(current_menu)
                current_menu = current_menu[index_item[user_choice]]
                break
            else:
                    user_choice = input('%s输入错误，请重新输入：%s' % (color_red, color_end))
    elif not isinstance(current_menu[item], dict):  # 如果菜单是最后一级，只能返回上级菜单或退出
        user_choice = input('输入"b"返回上级菜单，或输入"q"退出：').strip()
        while True:
            if user_choice.lower() == 'q':
                exit('%s感谢您的使用！%s' % (color_green, color_end))
            elif user_choice.lower() == 'b':
                current_menu = menus[-1]
                menus.pop()
                break
            else:
                user_choice = input('%s输入错误，请重新输入：%s' % (color_red, color_end))
    else:  # 如果菜单不是第一级也不是最后一级，可以返回上级菜单、进入下级菜单或退出
        user_choice = input('输入相应数字进入下级菜单，输入"b"返回上级菜单，输入"q"退出：').strip()
        while True:
            if user_choice.lower() == 'b':
                current_menu = menus[-1]
                menus.pop()
                break
            elif user_choice.lower() == 'q':
                exit('%s感谢您的使用！%s' % (color_green, color_end))
            elif user_choice not in index_item:
                user_choice = input('%s输入错误，请重新输入：%s' % (color_red, color_end))
            else:
                menus.append(current_menu)
                current_menu = current_menu[index_item[user_choice]]
                break
