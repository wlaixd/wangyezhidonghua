# _*_ coding: utf-8 _*_
"""
Time:     2025/2/7 15:31
Author:   Qin Liying
Version:  V 0.1
File:     文档目录自动更新.py
"""

import os
from win32com.client import Dispatch

def update_toc_hyperlinks(doc_path):
    # 打开 Word 应用程序
    word = Dispatch("Word.Application")
    word.Visible = False  # 设置为 False 以在后台运行

    try:
        # 打开文档
        doc = word.Documents.Open(doc_path)

        # 更新目录（TOC）
        for field in doc.Fields:
            if field.Type == 13:  # 13 是 TOC 字段的类型代码
                field.Update()

        # 更新目录中的超链接
        for field in doc.Fields:
            if field.Type == 13:  # 再次检查 TOC 字段
                # 以下代码假设目录是超链接格式，可能需要根据实际情况调整
                field.Select()
                word.Selection.Fields.Update()

        # 保存并关闭文档
        doc.Save()
        doc.Close()

        print(f"目录超链接已更新并保存: {doc_path}")
    except Exception as e:
        print(f"操作失败: {e}")
    finally:
        word.Quit()

# 示例：更新指定文档的目录超链接
doc_path = os.path.abspath("202412-丹莪妇康产品上市后研究报告.docx")  # 文档路径
update_toc_hyperlinks(doc_path)
