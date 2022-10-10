#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result


#check the above function
text = "ZSWX"
s = 4
cipher=encrypt(text,s)
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + cipher)
plain=""
for i in cipher:
    if(i.isupper()):
        plain+=chr(((ord(i)-s-65)%26)+65)
    else:
        plain+=chr(((ord(i)-s-97)%26)+97)
print("The plain text is",plain)

