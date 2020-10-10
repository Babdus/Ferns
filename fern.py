from tkinter import *
from math import cos, pi, sqrt

class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y

def outline(x, l, a, b):
	return (l*b/2)*(cos(pi*x/l)+a)

def stem(ref_p, l, w, o, n, d, max_d, b, dx):
	# print(''.join([' ' for i in range(d)]), ref_p.x, ref_p.y, l, w, o, n, d)
	x = sqrt(5)*l*2/sqrt(n)

	if o%4 == 0:
		ref_p = Point(ref_p.x-x, ref_p.y)
		canvas.create_line(ref_p.x+x, ref_p.y, ref_p.x+2*l, ref_p.y, fill="#336633", width=int(w))
	elif o%4 == 1:
		ref_p = Point(ref_p.x, ref_p.y-x)
		canvas.create_line(ref_p.x, ref_p.y+x, ref_p.x, ref_p.y+2*l, fill="#336633", width=int(w))
	elif o%4 == 2:
		ref_p = Point(ref_p.x+x, ref_p.y)
		canvas.create_line(ref_p.x-x, ref_p.y, ref_p.x-2*l, ref_p.y, fill="#336633", width=int(w))
	elif o%4 == 3:
		ref_p = Point(ref_p.x, ref_p.y+x)
		canvas.create_line(ref_p.x, ref_p.y-x, ref_p.x, ref_p.y-2*l, fill="#336633", width=int(w))
	if d == max_d:
		return
	last_x = -l
	for i in range(6, n):
		x = sqrt(i)*l*2/sqrt(n)-l
		l2 = outline(x,l,a,b)
		if l2 > dx*0.75:
			l2 = dx*0.75
		# if last_x is not None and x-last_x > l2/2 and x > 0:
		# 	break
		if l2 == 0:
			continue
		if o%4 == 0:
			ref_p2 = Point(ref_p.x+x+l, ref_p.y)
		elif o%4 == 1:
			ref_p2 = Point(ref_p.x, ref_p.y+x+l)
		elif o%4 == 2:
			ref_p2 = Point(ref_p.x-x-l, ref_p.y)
		elif o%4 == 3:
			ref_p2 = Point(ref_p.x, ref_p.y-x-l)
		stem(ref_p2, l2, w, o+((-1)**i), int(n/1.1), d+1, max_d, b, x-last_x)
		last_x = x

window = Tk()
 
window.title("Ideal Fern")

canvas = Canvas(window, width=1200, height=800, bd=0, highlightthickness=0)
canvas.configure(bg="white")
canvas.pack()

a = 1.25
b = 0.25

ref_p = Point(150, 400)

l = 450
w = 2

canvas.create_line(ref_p.x, ref_p.y, ref_p.x+2*l, ref_p.y, fill="#336633", width=w)

o = 0
n = 50

last_x = -l
for i in range(n):

	x = sqrt(i)*l*2/sqrt(n)-l
	l2 = outline(x,l,a,b)

	if x-last_x > l2/2 and x > 0:
		break

	if int(l2) == 0:
		continue
	ref_p2 = Point(ref_p.x+x+l, ref_p.y)
	stem(ref_p2, l2, w*1.5, o+((-1)**i), int(n/1.25), 1, 3, b, x-last_x)
	last_x = x

ref_p2 = Point(ref_p.x+x+l-(x-last_x)/2, ref_p.y)
stem(ref_p2, (l-x), w*1.5, o, int(n/2), 1, 3, b, 100)

window.mainloop()

