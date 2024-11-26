# python3.9
# -*- coding: UTF-8 -*-
"""
@Project ：useless_py 
@File    ：number_show.py
@Author  ：likm3
@Date    ：2024/11/26 09:17 
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

# 按钮回调函数
def on_confirm():
    try:
        # 获取输入框的值
        input_value = input_entry.get()
        if not input_value.isdigit():
            raise ValueError("请输入一个有效的整数！")
        input_value = int(input_value)

        # 更新进度条
        progress_bar['value'] = 0  # 重置进度条
        progress_bar['maximum'] = 10  # 设置最大值

        for i in range(1, progress_bar['maximum'] + 1):
            progress_bar['value'] = i
            root.update_idletasks()  # 刷新界面
            time.sleep(0.05)  # 模拟耗时任务

        # 弹窗提示输入的值
        messagebox.showinfo("输入值", f"您输入的值是：{input_value}")
    except ValueError as e:
        # 错误弹窗
        messagebox.showerror("错误", str(e))

# 创建主窗口
root = tk.Tk()
root.title("数值检测")
root.geometry("400x200")

# 输入框标签
input_label = tk.Label(root, text="请输入一个数值：", font=("Arial", 12))
input_label.pack(pady=10)

# 输入框
input_entry = tk.Entry(root, font=("Arial", 12), width=20)
input_entry.pack(pady=5)

# 确认按钮
confirm_button = tk.Button(root, text="确认", font=("Arial", 12), command=on_confirm)
confirm_button.pack(pady=10)

# 进度条
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)

# 启动主循环
root.mainloop()
