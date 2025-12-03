def cesar_cipher(text, key):

	crypted_text = ""
	for char in text:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_text += crypted_char

	return crypted_text


def cesar_uncipher(text, key):
	return cesar_cipher(text, -key)




crypted_text = cesar_cipher(text="lapin", key=3_000_000)
print(crypted_text)

initial_text = cesar_uncipher(text=crypted_text, key=3_000_000)
print(initial_text)