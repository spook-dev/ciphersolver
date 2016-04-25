import CipherSolverIncludes

ARGS = [2]

alphaL = "abcdefghijklnmopqrstuvqxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
num	= "0123456789"
keychars = num+alphaL+alphaU

def is_alpha(text):
	for i in text:
		if i.lower() not in "abcdefghijklmnopqrstuvwxyz ":
			return False
	return True

def check_if_valid(*args):
	args = list(args)
	if len(args[0]) == max(len(args[0]), len(args[1])):
		key = args[1]
		ct = args[0]
	else:
		key = args[0]
		ct = args[1]
	if not key.isalnum():
		return False
	return True

def decrypt(*args):
	args = list(args)
	if len(args[0]) == max(len(args[0]), len(args[1])):
		key = args[1]
		ct = args[0]
	else:
		key = args[0]
		ct = args[1]
	pt = ""
	for i in range(len(ct)):
		rotate_amount = keychars.index(key[i%len(key)])
		if ct[i] in alphaL:
			enc_char = ord('a') + (ord(ct[i])-ord('a')-rotate_amount + 52)%26
		elif ct[i] in alphaU:
			enc_char = ord('A') + (ord(ct[i])-ord('A')-rotate_amount + 52)%26
		elif ct[i] in num:
			enc_char = ord('0') + (ord(ct[i])-ord('0')-rotate_amount + 60)%10
		else:
			enc_char = ord(ct[i])
		pt = pt + chr(enc_char)
	certainty = min(CipherSolverIncludes.count_words(pt) / float(len(pt.replace("_", " ").split(" "))), 1.0)
	return CipherSolverIncludes.return_value(pt, "Trivial", certainty)

if __name__ == "__main__":
	print decrypt("YSAOEN:LG0CYI)FIHHTATESCO}RH{O", "a").plaintext
