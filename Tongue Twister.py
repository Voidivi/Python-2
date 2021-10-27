# !/usr/bin/env python3
# Assignment Week 2 - Tongue Twister
# Author: Lyssette  Williams

#Making the text and the dicitonary global so I do not have to call it into anything specifically

text = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked"
dictionary = {}

#display which will print the text, where the text is from and the 'table' headers
def display():
	print('"John Harris\'s Peter Piper\'s Practical Principles of Plain and Perfect Pronunciation (1813)"')
	print( )
	print(text)
	print( )
	print('Duplicates')
	print('Word  Count')

# main will run the y/n loop
def main():
	display()
	convert()
	cont_program = 'y'
	while cont_program == 'y' or cont_program == 'Y':
		twister()
		cont_program = input('Continue? (y/n): ')
		print('')
	print('Bye!')

# Twister seeks user input and then makes it lower case as well as providing the user what they are looking for
def twister():
  print(' ')
  userinput = input('Enter a word to find:').lower()
  if userinput in dictionary:
    print("Occurences:", dictionary[userinput])
  else:
    print('Occurences: 0')	
				
# Convert works the text which is global and inputs the words into the dictionary to be searched later

def convert():
	lcase = text.lower()
	for word in lcase.split():
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1
	for word in sorted(dictionary):
		if dictionary[word] > 1:
			print(word, dictionary[word])	

if __name__ == "__main__":
  main() 