import pytest

@pytest.mark.parametrize ("x1,y1,x2,y2,x,expected", [
	(0,0,1,1,2,2),
	(4,8,12,24,8,16),
	(0,0,5,0,7,0),
	(4,6,6,8,7,9),
	(1,3,1,6,0,"error"),
	])

def test_adder (x1,y1,x2,y2,x,expected):
	from addercalc import adder
	result = adder(x1,y1,x2,y2,x)
	assert result == expected
