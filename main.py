import string

def cesar_cipher(text, key, cipher=True):

	key = key if cipher else -key # ternary
	
	crypted_text = ""
	for char in text:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_text += crypted_char

	return crypted_text


def brute_force_cesar_cipher(crypted_text):
	for potential_key in range(1, 1_114_112):
		potential_initial_text = cesar_cipher(crypted_text, potential_key, cipher=False)

		for char in potential_initial_text:
			if char in string.printable:
				print(potential_key)
				print(potential_initial_text)
				print("-----")
				break




crypted_text = cesar_cipher(text="lapin", key=554)
print(crypted_text)

# initial_text = cesar_cipher(text=crypted_text, key=3_000_000, cipher=False)
# print(initial_text)


brute_force_cesar_cipher(crypted_text)