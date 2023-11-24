# -*- coding: utf-8 -*-
# reverse_cipher.py
# 反向密码脚本
# 此函数用于将输入的字符串反向输出，常见于简单的加密方法。

import sys

import pyperclip


def reverse_cipher(message):
    """
    将给定的消息反向加密。

    参数:
    message (str): 需要反向的原始消息字符串。

    返回:
    str: 反向后的消息字符串。
    """
    return "".join(reversed(message))


# 检查是否有命令行参数传入
if len(sys.argv) > 1:
    original_message = sys.argv[1]
else:
    # 如果没有命令行参数，使用默认消息
    original_message = "Three can keep a secret, if two of them are dead."

# 执行反向密码函数并打印结果
translated_message = reverse_cipher(original_message)

print("原始消息：", original_message)
print("反向消息：", reverse_cipher(original_message))

# 将转换后的消息复制到剪贴板
pyperclip.copy(translated_message)
