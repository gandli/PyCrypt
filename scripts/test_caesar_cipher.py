# -*- coding: utf-8 -*-
# test_caesar_cipher.py
import pytest

from caesar_cipher import SYMBOLS, caesar_cipher


# 基本加密和解密测试
def test_basic_encryption_decryption():
    original_message = "Hello, World!"
    key = 5
    encrypted = caesar_cipher(original_message, key, "encrypt", SYMBOLS)
    decrypted = caesar_cipher(encrypted, key, "decrypt", SYMBOLS)
    assert decrypted == original_message


# 边界条件测试
@pytest.mark.parametrize("key", [0, len(SYMBOLS)])
def test_boundary_key(key):
    message = "Boundary Test"
    result = caesar_cipher(message, key, "encrypt", SYMBOLS)
    assert result == message


# 特殊字符测试
def test_special_characters():
    message = "@#$%^&*()"
    result = caesar_cipher(message, 3, "encrypt", SYMBOLS)
    assert result == message


# 大密钥值测试
def test_large_key():
    message = "Large Key Test"
    key = len(SYMBOLS) + 5
    encrypted = caesar_cipher(message, key, "encrypt", SYMBOLS)
    decrypted = caesar_cipher(encrypted, key, "decrypt", SYMBOLS)
    assert decrypted == message


# 错误处理测试
def test_invalid_mode():
    with pytest.raises(ValueError):
        caesar_cipher("Test", 3, "invalid_mode", SYMBOLS)
