for i in range(1, 11): # i is an integer, range is a function
	print i

for j in [1, 2, 3]:
	print j

# Alternatively
for j in range(1, 4):
	print j

# use range to return the list [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for k in range(0, 20, 2):
	print k+2
	
#
for i in range(0, 4):
	print "****"
	
#################################
	
for i in range(1, 5):
		print "*" *i
for i in range(4, 0, -1):
	print "*" *i
	
#Write a function that takes a string and returns True if the string 
#contains the letter 'a', otherwise returns False. 
#Don't use Python's in operator, write the code yourself!

letters = raw_input( 'write a string of  characters: ')
print( 'You wrote' , letters )

for letter in letters:
	if letter == 'a':
		print 'True'
	else:
		 print 'False'
