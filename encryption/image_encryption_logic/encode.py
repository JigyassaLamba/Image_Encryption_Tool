import os, sys
from PIL import Image
from .utils import convert, add_zero

def encryptImage(parameter_list):
    cover_img_path = parameter_list[0]
    secret_img_path = parameter_list[1]
    op_path = 'media/encryption_result.png'
    print(cover_img_path, secret_img_path, op_path)
    cover_img = Image.open(cover_img_path)
    secret_img = Image.open(secret_img_path)
    encoded_image = encode(cover_img, secret_img)
    encoded_image.save(op_path)
    return op_path

def binary_pixel(img, width, height):
	encoded_pix = ''
	for i in range(width):
		for j in range(height):
			pixel = img[i, j]
			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			red_b, green_b, blue_b = convert(r, g, b)
			encoded_pix += red_b + green_b + blue_b
	return encoded_pix

def change(cover_img, encoded_pix, width1, height1, width_h, height_h):
	k = 0
	for i in range(width1):
		for j in range(height1):
			if j == 0 and i == 0:
				width_h_binary = add_zero(bin(width_h)[2:], 12)
				height_h_binary = add_zero(bin(height_h)[2:], 12)
				w_h_binary = width_h_binary + height_h_binary
				cover_img[i, j] = (int(w_h_binary[0:8], 2), int(w_h_binary[8:16], 2), int(w_h_binary[16:24], 2))
				continue
			r, g, b = cover_img[i, j]
			red_b, green_b, blue_b = convert(r, g, b)
			red_b = red_b[0:4] + encoded_pix[k:k+4]
			green_b = green_b[0:4] + encoded_pix[k+4:k+8]
			blue_b = blue_b[0:4] + encoded_pix[k+8:k+12]
			k += 12
			cover_img[i, j] = (int(red_b, 2), int(green_b, 2), int(blue_b, 2))
			if k >= len(encoded_pix):
				return cover_img
	# can never be reached, but let's return the image anyway
	return cover_img

def encode(cover_img, secret_img):
	encoded_image = cover_img.load()
	secret_img_copy = secret_img.load()
	width1, height1 = cover_img.size
	width_h, height_h = secret_img.size

	encoded_pix = binary_pixel(secret_img_copy, width_h, height_h)
	encoded_image = change(encoded_image, encoded_pix, width1, height1, width_h, height_h)
	return cover_img
