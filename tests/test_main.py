# raymond_calc_test

from calc import calc

case_numbers = [
    0, 1, 2, 4, 10, -1, -999999,
    9999999, 0.1, 0.999, 10000.0,
    -0.234, -1234.21313, 123.1232
]

case_adds = [
    '1+1', '1+3', '9999+9999', '1+1+1+1', '1+0.1',
    '0.1+0.1', '0.0000001+10000'
]

case_minus = [
    '1-1', '1-3', '9999-9999', '1-1-1-1', '1-0.1',
    '0.1-0.1', '0.0000001-10000'
]

case_add_minus = [
    '1-1+1', '-1+1', '0-1', '100-0.1+0.8', '-0.1-0.1-0.1'
]

def test_numbers():
    for cn in case_numbers:
        assert calc(str(cn)) == cn

def test_add():
    for ca in case_adds:
        assert calc(ca) == eval(ca)

def test_minus():
    for cm in case_minus:
        assert calc(cm) == eval(cm)

def test_add_minus():
    for cam in case_add_minus:
        assert calc(cam) == eval(cam)
