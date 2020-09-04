import pytest

@pytest.mark.parametrize ("(x1,y1)", [
	(0,0),
	(3,4),
	])
@pytest.mark.parametrize ("(x2,y2)", [
	(1,1),
	(6,8),
	])
@pytest.mark.parametrize ("x", [
	2,
	9,
	])
@pytest.mark.parametrize ("expected", [
	2,
	12,
	])

def test_adder ((x1,y1),(x2,y2),x,expected):
	from addercalc import adder
	result = adder((x1,x2),(x2,y2),x)
	assert result == expected