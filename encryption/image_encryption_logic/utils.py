def add_zero(binary, tot_length): # append zero to match string length 
	length = len(binary)
	return (tot_length - length) * '0' + binary

def convert(r, g, b): # convert decimal numbers of a pixel value to binary format
	return add_zero(bin(r)[2:], 8), add_zero(bin(g)[2:], 8), add_zero(bin(b)[2:], 8)