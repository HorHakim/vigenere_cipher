def cesar_cipher(text, key, cipher=True):

	key = key if cipher else -key # ternary
	
	crypted_text = ""
	for char in text:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_text += crypted_char

	return crypted_text






crypted_text = cesar_cipher(text="lapin", key=3_000_000)
print(crypted_text)

initial_text = cesar_cipher(crypted_text, 3_000_000, False)
print(initial_text)