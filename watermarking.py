from PIL import Image
import numpy



def get_image_even(image_array):
	return image_array - image_array % 2


def convert_text_to_binary(text):
	bits_str = "".join([bin(ord(char))[2:].zfill(21) for char in text])	
	list_of_bits = [int(bit) for bit in bits_str]
	return list_of_bits


def watermark_image(image_array, text):
	even_array_image = get_image_even(image_array)
	list_of_bits = convert_text_to_binary(text)

	number_rows, number_cols, number_canals = even_array_image.shape

	for row in range(0, number_rows):
		for col in range(0, number_cols):
			for canal in range(0, number_canals):
				if list_of_bits :

					even_array_image[row][col][canal] += list_of_bits.pop(0)

	if list_of_bits:
		print("Ecriture du message incomplète !")


	Image.fromarray(even_array_image).save('image_watermarked.png')




def get_message_from_watermarked_image(image_watermarked_array):
	initial_binary_message = "".join(str(bit) for bit in image_watermarked_array.flatten() % 2)

	list_of_char = []
	for index in range(0, len(initial_binary_message), 21):
		binary_token = initial_binary_message[index: index+21]
		list_of_char.append(chr(int(binary_token, 2)))
		if binary_token == "0"*21:
			break

	return "".join(list_of_char)






if __name__ == "__main__":
	image = Image.open("./image.png").convert('RGB')
	image_array = numpy.array(image)
	watermark_image(image_array, text="chocolat")


	image_watermarked = Image.open("./image_watermarked.png").convert('RGB')
	image_watermarked_array = numpy.array(image_watermarked)
	print(get_message_from_watermarked_image(image_watermarked_array))







