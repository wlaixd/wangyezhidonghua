
"""
Warning: 该脚本仅模拟点击, 无任何判断逻辑(即仍需人工审核)
"""


import keyboard
import pyautogui as pg
import time
import sys

# 定义控制程序暂停和继续执行的函数
def pause_program():
    global is_paused
    is_paused = True1
    print("Program paused. Press 'a' to continue or 'q' to exit.")

def continue_program():
    global is_paused
    is_paused = False
    print("Program continued.")

# 定义函数来处理退出逻辑
def exit_program():
    print("Exiting program...")
    sys.exit()

# 设置按键
continue_run = '3'  # 继续执行
pause_run = '2'    # 暂停程序
end_run = '1'      # 退出程序
is_paused = False  # 记录程序是否处于暂停状态

def func1():
    # 设定检测新数据出现的坐标（这里已按你提供的坐标设置，你可按需调整）
    check_x, check_y = 1707, 478
    # 设定初始的目标颜色
    target_color = (255, 255, 255)

    while True:
        # 第一步：点击初始位置（假设这个操作会触发新数据出现）
        pg.moveTo(1780, 340, duration=0.5)
        pg.click(button='left')
        time.sleep(0.5)  # 等待一段时间，假设新数据在这期间出现并加载完成

        # 获取检测坐标点的当前颜色 目标坐标点的颜色发生变化，则退出循环
        current_color = pg.pixel(check_x, check_y)
        if current_color != target_color:
            break

    keyboard.on_press_key(pause_run, lambda _: pause_program())  # 暂停键（'d'）
    keyboard.on_press_key(continue_run, lambda _: continue_program())  # 继续键（'a'）
    keyboard.on_press_key(end_run, lambda _: exit_program())  # 退出键（'q'）

    while True:
        if is_paused:
            time.sleep(0.5)  # 处于暂停状态时，短暂等待一下再检查状态
            continue
        # 第二步：点击新数据出现后的第一个新位置（假设坐标为 (1800, 400)）
        pg.moveTo(1757, 475, duration=0.1)
        pg.click(button='left')
        time.sleep(0.5)  # 停顿一下，确保点击生效，也可以根据实际情况调整等待时间

        # 第三步：点击另一个新位置（假设坐标为 (1900, 500)）
        pg.moveTo(1180, 255, duration=0.5)
        pg.click(button='left')
        time.sleep(0.5)


if __name__ == "__main__":
    func1()
