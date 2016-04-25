import CipherSolverIncludes

ARGS = [1]

def check_if_valid(in_val):
	try:
		in_val.decode("base64")
	except:
		return False
	return True

def decrypt(in_val):
	plain = in_val.decode("base64")
	count, r_frequency, f_table = CipherSolverIncludes.readable_character_frequency(plain)
	return CipherSolverIncludes.return_value(plain, "base64", r_frequency)
