import sys

raw_text = sys.argv[1]

print "raw_text",raw_text

encoded_text = []

#encryption scheme
for char in raw_text:
	encoded_text.append(chr(ord(char) + 4))

#turns character array into a string
encoded_text = ''.join(encoded_text)

decoded_text = []

#decryption scheme
for char in encoded_text:
	decoded_text.append(chr(ord(char) - 4))

#turns character array into a string
decoded_text = ''.join(decoded_text)

#print everything
print "encoded_text", encoded_text
print "decoded_text", decoded_text
