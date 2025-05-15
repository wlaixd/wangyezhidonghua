# _*_ coding: utf-8 _*_
"""
Time:     2025/2/11 16:26
Author:   Qin Liying
Version:  V 0.1
File:     系统报告填写.py
"""

# def convert_input_to_dict(text):
#     # 将输入字符串按行分割
#     lines = text.strip().split("\n")
#
#     # 初始化空字典
#     chlorpromazine_report = {}
#
#     # 遍历每一行，分割键和值，并填入字典
#     for line in lines:
#         if "：" in line:  # 检查是否包含中文冒号
#             key, value = line.split("：", 1)
#             chlorpromazine_report[key.strip()] = value.strip()  # 去除可能的空白字符
#
#
#     # return chlorpromazine_report
#     return chlorpromazine_report
# def clean(chlorpromazinereport):
#     # 现有Excel文件的路径
#     import pandas as pd
#     excel_file_path = 'hhh.xlsx'
#
#     # 读取Excel文件
#     df = pd.read_excel(excel_file_path)
#
#     # 将字典转换为DataFrame，并将其设置为第二行（索引为1）
#     df.loc[1] = pd.Series(chlorpromazinereport)
#
#     # 将更新后的DataFrame保存回Excel文件
#     df.to_excel(excel_file_path, index=False)
#     return df.head()
#
#
#
# # 字典数据
#
# # # 模拟的输入数据
# text = input("输入老板任务:")
# convert_input_to_dict(text)
# clean(convert_input_to_dict(text))



import pyautogui
import time

# 给用户一些时间切换到正确的窗口
time.sleep(1)



# 垂直向下滚动鼠标1000个单位
pyautogui.click(1833,643)
pyautogui.scroll(-1000)
#起始样本
pyautogui.click(1835,916)
pyautogui.click(1419,860)
pyautogui.press('0')

#样本量
pyautogui.click(138,330)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1613,858)
pyautogui.hotkey('ctrl', 'v')



pyautogui.click(1852,922)
pyautogui.click(1833,643)

#向上平移5000确保下一个界面
pyautogui.scroll(5000)

# 定义一个列表，包含所有自定义的坐标
click_positions = [
    (146, 238),  # 第1次点击的坐标
    (146, 259),
    (146, 275),
    (146, 296),
    (146, 312),
    (146, 330),
]


# 给用户一些时间切换到正确的窗口
# time.sleep(5)

# 定义一个列表，包含所有自定义的点击坐标

# 定义一个列表，包含所有自定义的粘贴坐标
paste_positions = [
    (1349, 399),  # 第1次粘贴的坐标
    (1349, 469),  # 第2次粘贴的坐标
    (1349, 559),  # 第3次粘贴的坐标
    (1349, 624),  # 第4次粘贴的坐标
    (1349, 749),  # 第5次粘贴的坐标
    (1349, 836)  # 第5次粘贴的坐标

]

# 确保两个列表的长度相同
assert len(click_positions) == len(paste_positions), "点击坐标和粘贴坐标的数量必须相同"

# 循环次数与坐标列表长度相同
for click_pos, paste_pos in zip(click_positions, paste_positions):
    # 移动鼠标到指定位置并点击
    pyautogui.click(click_pos)

    # 使用ctrl+c复制文本
    pyautogui.hotkey('ctrl', 'c')

    # 稍作延迟，确保复制操作完成
    time.sleep(0.1)

    # 移动鼠标到粘贴位置并点击
    pyautogui.click(paste_pos)

    # 使用ctrl+v粘贴文本
    pyautogui.hotkey('ctrl', 'v')

    # 如果需要，在此处添加额外的延迟
    time.sleep(0.1)  # 例如，每次操作后暂停1秒

#确认生成
pyautogui.click(1835,916)

