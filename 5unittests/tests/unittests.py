import basics
import sys

def test_positive():
    assert basics.square(2) == 4
    assert basics.square(3) == 9

def test_negative():
    assert basics.square(-2) == 4
    assert basics.square(-3) == 9

def test_zero():
    assert basics.square(0) == 0

"""
def test_str():
    with pytest.raises(TypeError):
        basics.square("cat")
"""
print(sys.path)