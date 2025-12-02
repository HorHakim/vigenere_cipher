def cesar_cipher(text, key):

	crypted_text = ""
	for char in text:
		crypted_char = chr(ord(char) + key)
		crypted_text += crypted_char

	return crypted_text

crypted_text = cesar_cipher(text="lapin", key=3)
print(crypted_text)