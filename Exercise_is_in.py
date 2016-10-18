# find out if a character is in a string, so long as the string is sorted in alphabetical order, return a boolean value

def isIn(char, aStr):

 # Base check, if the string is blank return False, if the string is == to 1 return the string is equal to char
 
	if aStr == '':
		return False
	if len(aStr) == 1:
		return aStr == char
    
  # find the middle char in the string
  
	mid = len(aStr) // 2
	midChar = aStr[mid]
  
  # if the character == the middle char it is in the string
  
	if char == midChar:
		return True
    
    # if the char is les than the mid only check the first half of the string, else check the second half
    
	elif char < midChar:
		return isIn(char, aStr[:mid])
	else:
		return isIn(char, aStr[mid])
    
