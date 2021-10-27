#!/usr/bin/env python3
#Assignment Week 4 - Exceptional Exception Handling
#Author: Lyssette  Williams


###################################################################################
#  Exceptional program
#  A truly exceptional program that throws exceptions at every turn.
#
#  Date: 2/21/21
###################################################################################


###################################################################################
# Function: read_something
# Input:  filename
# TODO - fix when unsuccessfully tries to open a file that doesn't exist

###################################################################################
def read_something(filename):
  try:
    with open(filename) as file:
      read_data = file.read()
  except FileNotFoundError:
    print('Could not find the file named', filename)
  except OSError:
    print('Fild found - error reading file')
  except Exception:
    print('An unexpected error occured')       

###################################################################################
# Function: checkit
# Input:  an exceptional number
# TODO - fix does nothing with its input but throw an exception 
###################################################################################
def checkit(threshold):
  x = 42
  try:
    if x > 5:
      raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
  except Exception as e: #I'm not sure if this was the right thing to add but it made it so main would finish running
    print(type(e), e)     

###################################################################################
# Function: calculate_something
# Input:  none
# TODO - fix prints result in ZeroDivision error
###################################################################################
def calculate_something():
  try:  
    print(0/0)
  except ZeroDivisionError:
    print('Division by Zero found')  
###################################################################################
# Function: main
# Output:  Demonstrates draw_wordcloud, save_wordcloudfile and view_wordcloudfile
#    output is written to "outfile.png" in directory it was run
#    displays popup on screen and windows should be closed to continue  
###################################################################################
def main():

    print("[Exceptional] A Truly Exceptional Module")
    read_something("myfile.txt")
    checkit(15)
    calculate_something()
    print("[Exceptional] Successfully (?) completed!")
    
if __name__ == "__main__":
    main()  
