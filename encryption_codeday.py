import random
def encrypt(plaintext,shift, whichOneToAdd):
	words = plaintext.split(" ")
	for word in words:
		print(encryptWord(word, shift, whichOneToAdd))

def encryptWord(plaintext, shift, whichOneToAdd):
	ordarray = []
	new = ""
	#shift word using alphabet
	for char in plaintext:
		n = ord(char) + shift
		if n > 122:
			n = n - 26
		new += chr(n)

	#if(ord(new[-1])%2): # if last letter's ASCII code is odd
		#new += chr(random.randint(97,122))

	#get the ASCII values for each letter
	for i in new:
		ordarray.append(ord(i))

	#mess up frequency precidtion
	for z in range(0, len(ordarray)):
		if z%whichOneToAdd:
			ordarray[z] = ordarray[z] + 1

	#input the messed up prediction into an equation to produce big numbers
	#this will make it harder to brute force since the hacker needs the inverse equation to brute force
	# for r in range(0, len(ordarray)):
		# ordarray[r] = 2*(ordarray[r])**3 + 2.5*(ordarray[r])**2 + 9*(ordarray[r])-5

	return ordarray

encrypt("troll hard", 2, 2)

def decrypt(crypted, keyShift, keyAdded):
	original = "";
	for i in range(0,len(crypted)):
		if i % keyAdded:
			crypted[i] -= 1;
		crypted[i] -= keyShift
		if crypted[i] > 122:
			crypted[i] -= 25
		original += chr(crypted[i])
	return original
