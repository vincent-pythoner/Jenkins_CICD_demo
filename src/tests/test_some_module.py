# test_some_module.py
from ..some_module import add, subtract

def test_add():
    assert add(1, 2) == 3  # 测试了 add 函数

def test_subtract():
    assert subtract(5, 3) == 2  # 测试了 subtract 函数

