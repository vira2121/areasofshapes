import assign

def test_rect():
    x=5
    y=7
    result=assign.rectangle(x,y)
    assert x*y==result

def test_periRec():
    x=5
    y=8
    result=assign.perimeter_rect(x,y)
    assert 2*(x+y)==result

def test_areaSquare():
    x=8
    result=assign.area_square(x)
    assert x*x==result