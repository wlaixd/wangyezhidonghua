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


if __name__ == "__main__":
    # 定义考核事项配置（放在主程序中）
    assessment_items = [
        ([584, 324], "知识运维，及时完成样本审核"),
        ([579, 384], "知识应用，及时准确出具报告"),
    ]

    txt = """完善报告生成脚本，完成报告所需数据清洗3000例，30%
清零超过1个工作日的样本审核，20%
2个工作日内完成企业报告出具或修订，40%
积极转发5个以上公司宣导内容，10%
    """

    osa(txt, assessment_items)