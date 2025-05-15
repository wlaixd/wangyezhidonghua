import pyautogui as pg
import time
import pyperclip as pc
import re


def click(pos, t=0.1):
    pg.moveTo(pos[0], pos[1], duration=0.1)
    pg.click(button='left')
    time.sleep(t)


def ctrl_v(text):
    pc.copy(text)
    pg.hotkey("ctrl", "v")
    time.sleep(0.1)


def osa(text, assessment_items):
    # 打开osa填写界面
    click([150, 216], t=0.5)
    click([150, 256], t=0.5)
    click([350, 398])
    pg.scroll(1000)

    # 添加内容
    for i in [[452, 379], [452, 447], [452, 575], [452, 667], [452, 760], [452, 927]]:
        click(i)
    pg.scroll(-1000)

    # 提取信息
    pattern1 = "(.+)，"
    pattern2 = r"，(\d+)"
    content1 = re.findall(pattern1, text)
    content2 = re.findall(pattern2, text)

    # 填充考核事项（从主程序传入配置）
    for coord, text in assessment_items:
        click(coord)
        ctrl_v(text)

    # 填充考核指标
    for i, j in enumerate([[600, 519], [600, 613], [600, 704], [600, 875]]):
        click(j)
        ctrl_v(content1[i].strip("\n "))

    for i, j in enumerate([[600, 556], [600, 649], [600, 738], [600, 903]]):
        click(j)
        ctrl_v(content2[i])
    click([935, 1009])
import re

# 定义文本字符串


# 将文本按行分割成列表

def clean(tet):
    tasks_list = tet.split('\n')
    tasks_list = [task for task in tasks_list if not task.startswith("O")]

    # 初始化一个新列表来存储过滤后的行
    newlines = []

    # 遍历每一行
    for text in tasks_list:
        # 使用正则表达式替换掉以数字加点开头的文本
        text = re.sub(r"^\d+\.", "", text)
        # 将处理后的行添加到新列表
        newlines.append(text)

    return newlines

def change(percentages):
    tasks = clean(tet)

    # 添加额外的任务和百分比
    tasks.append('积极转发5个以上公司宣导内容')
    percentages.append('10%')

    # 拼接字符串
    txt = ""
    for task, percentage in zip(tasks, percentages):
        txt += f"{task}，{percentage}\n"

    # 去掉最后一个换行符
    txt = txt.rstrip()
    print(txt)
    return txt






if __name__ == "__main__":
    # 定义考核事项配置（放在主程序中）
    assessment_items = [
        ([584, 324], "知识运维，及时完成样本审核"),
        ([579, 384], "知识应用，及时准确出具报告"),
    ]
    tet = '''O1数据运维，及时完成样本审核
1.清零超过1个工作日的样本审核
O2数据应用，及时准确出具报告
1.2个工作日内完成企业报告出具或修订
2.完善报告生成脚本，完成报告所需数据清洗3000例
O3公司领导交待的其他事项'''
    percentages = ["40%", "30%", "20%"]

    print(clean(tet))
    change(percentages)
    # print(txt)
#     txt = """完善报告生成脚本，完成报告所需数据清洗3000例，30%
# 清零超过1个工作日的样本审核，20%
# 2个工作日内完成企业报告出具或修订，40%
# 积极转发5个以上公司宣导内容，10%
#     """

    osa(change(percentages), assessment_items)
