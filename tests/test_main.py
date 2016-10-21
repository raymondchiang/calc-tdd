from calc import calc

case_numbers = [
    0, 1, 2, 4, 10, -1, -999999,
    9999999, 0.1, 0.999, 10000.0,
    -0.234, -1234.21313, 123.1232
]

case_adds = [
    '1 + 1', '1+3', '9999+9999', '1+1+1+1', '1+0.1','0+1',
    '0.1+0.1', '0.0000001+10000', '1 + 1', '1+ 1', '1 +1',
    '1+ 0.1',
]

case_minus = [
    '1-1', '1-3', '9999-9999', '1-1-1-1', '1-0.1',
    '0.1-0.1', '0.0000001 - 10000',
]

case_add_minus = [
    '1-1+1', '-1+1', '0-1', '100-0.1+0.8', '-0.1-0.1-0.1',
]

case_mutli = [
    '1*1', '1*1+450*0.2+9*10', '1*0', '0*1', '1*0.1', '0*0',
    '0.0001*10000', '100*1*0*123', '0*0*0*2', '1 * 1 * 11',
]

case_divide = [
    '1/1', '1/1+450/0.2+9/10', '0/1', '1/0.1',
    '0.0001/10000', '100*1/123', '0*0*0/2',
    '123+2123 / 223+234+213-221', '1/-1', '1/-1*-1',
    '1/-1*-1',
]

case_parentheses =[
    '( - 10 + 8 )','(-10+8*10)','-1*(-10+8*10)','-1*(-1*(-10+8*10))',
    '-1*(-1*(-10+8/10))','(-10+8*10)+30/10+9','-1*(-10+8*10)+30/(10+9)',
    '((-10+8*10)+30/(10+9))/((-10+8*10)+30/(10+9))-1',
    '( ( -10 + 8 * 10 ) + 30 / ( 10+9  ) ) / ( ( - 10 + 8 * 10 ) + 30 / ( 10+9 ) ) - 1',
]

case_special =[
    '-(1(-2(-3(4+1))))','-(2(2))+(3(3))-(3(3))+(2(2))',
    '-01(-(10)+000002)','-9 87(98 7/9 8 7)+(2222)',
]
#----------------------------------
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

def test_mutli():
    for cm in case_mutli:
        assert calc(cm) == eval(cm)

def test_divide():
    for cm in case_divide:
        assert calc(cm) == eval(cm)

def test_parentheses():
    for cp in case_parentheses:
        assert calc(cp)==eval(cp)
