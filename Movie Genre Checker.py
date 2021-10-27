# !/usr/bin/env python3
# Assignment Week 3 - Working with Files
# Author: Lyssette  Williams

#importing csv and making the dictionary global
import csv
dictionary = {}

#defining the display for the generator
def display():
	print('Movie Genre Data')
	print(' ')
	print('Word  Count')

#looking for user input
def userquery():
	print(' ')
	userinput = input('Enter a movie genre:').capitalize()
	if userinput in dictionary:
		print('Occurrences:', dictionary[userinput])
	else:
		print('That genre does not exist in our database. Try again.')	

#this will be reading the csv file provided
#this took a while because I didn't realize every row of the csv was a dictionary
def read_file():
	with open('imdb_genre.csv', 'r') as file:
		reader = csv.DictReader(file)	
		for row in reader:
			genre = row.get('Genre')
			if genre in dictionary:
				dictionary[genre] += 1
			else: 
				dictionary[genre] = 1
	for word in sorted(dictionary):
		if dictionary[word]	> 1:
			print(word, dictionary[word])


# this will write into a new txt file and it will also overwrite a previously existing file everytime it runs
def write_file():
	with open('summary_lwilliams.txt', 'w') as file:
		for genre in sorted(dictionary):
			file.write(genre + ' ' + str(dictionary[genre]) + '\n')

#running the entire program
def main():
	display()
	read_file()
	write_file()
	cont_progam = 'y'
	while cont_progam == 'y' or cont_progam == 'Y':
		userquery()
		cont_progam = input('Continue? (y/n): ')
		print(' ')
	print('Bye')


if __name__ == "__main__":
  main() 
