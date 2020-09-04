def find_y (x1,y1,x2,y2,x):
	if (x1==x2):
		return "error"
	m = calc_m (x1,x2,y1,y2)
	b = calc_b (x1,x2,y1,y2,m)
	y = m*x + b
	return y

def calc_m (x1,x2,y1,y2):
	m = (y2-y1)/(x2-x1)
	return m

def calc_b (x1,x2,y1,y2,m):
	b = y1 - m*x1
	return b