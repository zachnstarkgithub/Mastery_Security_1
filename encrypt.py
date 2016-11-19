import sys

raw_text = sys.argv[1]

print "raw_text",raw_text

encoded_text = []
for char in raw_text:
	encoded_text.append(chr(ord(char) + 4))
encoded_text = ''.join(encoded_text)

decoded_text = []
for char in encoded_text:
	decoded_text.append(chr(ord(char) - 4))
decoded_text = ''.join(decoded_text)

print "encoded_text", encoded_text
print "decoded_text", decoded_text
