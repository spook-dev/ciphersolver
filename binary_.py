import CipherSolverIncludes
from RSA_ import to_text
from RSA_ import to_num

ARGS = [1]

def check_if_valid(in_val):
	chars = []
	for i in in_val:
		if not i in chars:
			chars.append(i)
	if len(chars) <= 2:
		return True
	return False

def decrypt(in_val):
	chars = []
	for i in in_val:
		if not i in chars:
			chars.append(i)
	zero = chars[0]
	one = chars[1]
	text1 = ""
	text2 = ""
	for i in in_val:
		if i == zero:
			text1 += "0"
		elif i == one:
			text1 += "1"
	for i in in_val:
		if i == zero:
			text2 += "1"
		elif i == one:
			text2 += "0"
	text1 = to_text(int(text1, 2))
	text2 = to_text(int(text2, 2))
	c1, r1, f1 = CipherSolverIncludes.readable_character_frequency(text1)
	c2, r2, f2 = CipherSolverIncludes.readable_character_frequency(text2)
	if c1 > c2:
		return CipherSolverIncludes.return_value(text1, "Binary substitution %s = 0, %s = 1" % (zero, one), r1)
	elif c2 > c1:
		return CipherSolverIncludes.return_value(text2, "Binary substitution %s = 0, %s = 1" % (one, zero), r2)
	else:
		return CipherSolverIncludes.return_value(text1 + " /OR/ " + text2, "Binary substitution. Both substitutions shown", (r1 + r2) / 2)
if __name__ == "__main__":
	print decrypt("1110100011010000110100101110011001000000110100101110011001000000111010001101111011101000110000101101100011011000111100100100000011000010010000001100110011011000110000101100111").plaintext
