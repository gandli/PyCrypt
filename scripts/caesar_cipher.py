# -*- coding: utf-8 -*-
# caesar_cipher.py
# 凯撒密码脚本
# 此脚本用于将输入的字符串进行凯撒密码加密或解密。

import sys

import pyperclip


def caesar_cipher(message, key, mode, symbols):
    """
    执行凯撒密码的加密或解密。

    参数:
    message (str): 需要加密或解密的原始消息字符串。
    key (int): 字母移动的位置数。
    mode (str): 'encrypt' 为加密模式，'decrypt' 为解密模式。
    symbols (str): 可用于加密或解密的字符集。

    返回:
    str: 加密或解密后的消息字符串。
    """
    if mode not in ["encrypt", "decrypt"]:
        raise ValueError("模式必须是 'encrypt' 或 'decrypt'")

    if mode == "decrypt":
        key = -key

    translated = ""
    for symbol in message:
        if symbol in symbols:
            symbol_index = symbols.find(symbol)
            translated_index = (symbol_index + key) % len(symbols)
            translated += symbols[translated_index]
        else:
            translated += symbol

    return translated


# 定义可能被加密的符号
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# 检查是否有命令行参数传入
if len(sys.argv) > 3:
    original_message = sys.argv[1]
    key = int(sys.argv[2])
    mode = sys.argv[3]
else:
    # 如果没有命令行参数，使用默认消息、密钥和模式
    original_message = "This is my secret message."
    key = 13
    mode = "encrypt"

# 执行凯撒密码加密/解密并打印结果
translated_message = caesar_cipher(original_message, key, mode, SYMBOLS)
print("原始消息：", original_message)
print("转换后的消息：", translated_message)

# 将转换后的消息复制到剪贴板
pyperclip.copy(translated_message)
