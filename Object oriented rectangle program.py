# !/usr/bin/env python3
# Assignment Week 5 - Object Oriented Rectangle Program
# Author: Lyssette  Williams

#defining the class rectangle which we will use later
class Rectangle:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def getPerimeter(self):
		return 2 * (self.length+self.width)
	
	def getArea(self):
		return self.length * self.width

#code provided in the assignment specs
	def getStr(self):
		mystr = ""
		width = "* " * self.width + "\n"
		mystr += width
		for i in range(self.length-2):
			mystr += "* "
			mystr += "  " * (self.width-2)
			mystr += "* \n"
		mystr += width
		return mystr	   

# program display function
def display():
	print('Rectangle Calculator')
	print('='*35)

# This does all the talking to the user and rectangle stuff
# I added a try/except since we just did that last time 
# and then also wanted to make sure we wouldn't have to deal with a rogue negative number
def define():
	try:
		length = int(input('Height: '))
		width = int(input('Width: '))
	except ValueError:
		print('Opps! You must enter an integer.')
		return	
	if length < 0 or width < 0:
		print('Your integer must be positive.')	
		return
	shape = Rectangle(length,width)
	area = shape.getArea()
	perimeter = shape.getPerimeter()
	print('Perimeter: ', perimeter)
	print('Area: ', area)
	print(shape.getStr())

#main runs the whole program
def main():
	display()
	cont_progam = 'y'
	while cont_progam == 'y' or cont_progam == 'Y':
		define()
		cont_progam = input('Continue? (y/n): ')
		print(' ')
	print('Bye!')

if __name__ == "__main__":
  main() 
