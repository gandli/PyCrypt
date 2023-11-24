# test_reverse_cipher.py

import pytest
from reverse_cipher import reverse_cipher


# 测试正常字符串
def test_normal_string():
    message = "Hello, World!"
    expected = "!dlroW ,olleH"
    assert reverse_cipher(message) == expected


# 测试空字符串
def test_empty_string():
    message = ""
    expected = ""
    assert reverse_cipher(message) == expected


# 测试特殊字符
def test_special_characters():
    message = "!@#$%^&*()_+"
    expected = "+_)(*&^%$#@!"
    assert reverse_cipher(message) == expected


# 测试边缘情况
@pytest.mark.parametrize("message", ["a", "ab", "1234567890" * 100])
def test_edge_cases(message):
    assert reverse_cipher(reverse_cipher(message)) == message
