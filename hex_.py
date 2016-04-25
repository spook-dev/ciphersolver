import CipherSolverIncludes

ARGS = [1]
def check_if_valid(in_val):
	if type(in_val) != type(""):
		return False
	in_val = in_val.lower()
	for i in in_val:
		if i not in "0123456789abcdef":
			return False
	if len(in_val) % 2 == 1:
		in_val = in_val + "0"
	return True

def decrypt(in_val):
	if len(in_val) % 2 != 0:
		in_val = "0" + in_val
	plaintext = in_val.decode("hex")
	c, r, f = CipherSolverIncludes.readable_character_frequency(in_val.decode("hex"))
	return CipherSolverIncludes.return_value(plaintext, "hexidecimal", r)

