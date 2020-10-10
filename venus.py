from tkinter import *
from functools import partial
from math import sqrt, sin, cos, pi
import random
import time


class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y

	def translate(self, a, l):
		return Point(self.x+cos(a)*l, self.y+sin(a)*l)

	def move(self, a, l):
		self.x = self.x+cos(a)*l
		self.y = self.y+sin(a)*l

	def midpoint(p1, p2):
		return Point(p1.x-(p1.x-p2.x)/2, p1.y-(p1.y-p2.y)/2)


def fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def stem_len(n):
	return ((fib(n)**(1/6))+1)*2-3


def draw_line(canvas, p1, p2):
	line = canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="#223322", width=3)
	return line


def draw_circle(canvas, center, radius, leaf_color):
	circle = canvas.create_oval(center.x-radius,
								center.y-radius,
								center.x+radius,
								center.y+radius,
								fill=leaf_color, width=0)
	return circle


def draw_circle_shaddow(canvas, center, radius, shaddow, leaf_color):
	circle = canvas.create_oval(center.x-radius-shaddow,
								center.y-radius-shaddow,
								center.x+radius+shaddow,
								center.y+radius+shaddow,
								fill=leaf_color, width=0, stipple="gray75")
	return circle


def draw_n_pinna(canvas, n, point, direction, orientation, angle, scale, radius, leaf_color, objects):
	if n < 1:
		raise Exception
	length = stem_len(n)*scale
	point2 = point.translate(direction, length)
	line = draw_line(canvas, point, point2)
	objects.append(line)
	if radius > 0:
		midpoint = Point(point.x, point.y)
		for i in range(int(length)):
			circle = draw_circle_shaddow(canvas, midpoint, radius, 3, leaf_color)
			objects.append(circle)
			midpoint.move(direction, 1)
	elif n < 5:
		midpoint = Point.midpoint(point, point2)
		for i in range(int(length/2)):
			radius = 2*i/3
			circle = draw_circle_shaddow(canvas, midpoint, radius, 3, leaf_color)
			objects.append(circle)
			midpoint.move(direction, 1)
	if n > 2:
		n2 = n

		if n > 5:
			n2 -= 1
		if n > 9:
			n2 -= 1
		if n > 15:
			n2 -= 1
		if n > 23:
			n2 -= 1
		draw_n_pinna(canvas, n2-2, point2, direction+angle*orientation, -orientation, angle, scale, radius, leaf_color, objects)
		draw_n_pinna(canvas, n-1, point2, direction-angle*orientation, -orientation, angle, scale, radius, leaf_color, objects)

	# if radius > 0:
	# 	midpoint = Point(point.x, point.y)
	# 	for i in range(int(length)):
	# 		draw_circle(canvas, midpoint, radius, leaf_color)
	# 		midpoint.move(direction, 1)
	# elif n < 5:
	# 	midpoint = Point.midpoint(point, point2)
	# 	for i in range(int(length/2)):
	# 		radius = 2*i/3
	# 		draw_circle(canvas, midpoint, radius, leaf_color)
	# 		midpoint.move(direction, 1)

def grow_venus_hair_fern(canvas, window):
	objects = []

	x, y, n = random.randint(200,1000), random.randint(-150, 0), random.randint(15, 20)

	for i in range(1, n):
		for obj in objects:
			canvas.delete(obj)
		draw_n_pinna(canvas, i, Point(x, y), pi/2, 1, pi/8, 12, 0, "#66cc55", objects)
		window.update()
		time.sleep(0.2)

def main():
	window = Tk()
	window.title("Adiantum Capillus-Veneris")
	canvas = Canvas(window, width=1200, height=1000, bd=0, highlightthickness=0)
	canvas.configure(bg="#000812")
	canvas.pack()

	# for i in range(5):
	# 	x, y, n = random.randint(0,1200), random.randint(-150, -50), random.randint(15, 18)
	# 	objects = []

	# 	for i in range(1, n):
	# 		for obj in objects:
	# 			canvas.delete(obj)
	# 		draw_n_pinna(canvas, i, Point(x, y), pi/2, 1, pi/8, 7, 0, "#1b4a44", objects)
	# 		window.update()
	# 		time.sleep(0.01)
	# for i in range(5):
	# 	x, y, n = random.randint(0,1200), random.randint(-150, -50), random.randint(14, 17)
	# 	objects = []

	# 	for i in range(1, n):
	# 		for obj in objects:
	# 			canvas.delete(obj)
	# 		draw_n_pinna(canvas, i, Point(x, y), pi/2, 1, pi/8, 8, 0, "#276357", objects)
	# 		window.update()
	# 		time.sleep(0.01)
	# for i in range(4):
	# 	x, y, n = random.randint(0,1200), random.randint(-150, -50), random.randint(13, 16)
	# 	objects = []

	# 	for i in range(1, n):
	# 		for obj in objects:
	# 			canvas.delete(obj)
	# 		draw_n_pinna(canvas, i, Point(x, y), pi/2, 1, pi/8, 9, 0, "#327a62", objects)
	# 		window.update()
	# 		time.sleep(0.01)
	# for i in range(4):
	# 	x, y, n = random.randint(0,1200), random.randint(-150, -50), random.randint(12, 17)
	# 	objects = []

	# 	for i in range(1, n):
	# 		for obj in objects:
	# 			canvas.delete(obj)
	# 		draw_n_pinna(canvas, i, Point(x, y), pi/2, 1, pi/8, 11, 0, "#3f966c", objects)
	# 		window.update()
	# 		time.sleep(0.01)
	# for i in range(5):
	# 	draw_n_pinna(canvas, 15, Point(random.randint(200,1000), random.randint(-150, 0)), pi/2, 1, pi/8, 13, 0, "#4cb56a")

	grow_venus_hair_fern(canvas, window)

	button1 = Button(window, text = "Grow", command = partial(grow_venus_hair_fern, canvas, window), anchor = W)
	button1.configure(width = 10, activebackground = "#66cc55", relief = FLAT)
	button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)

	window.mainloop()

main()