import CipherSolverIncludes

ARGS = [2]

def check_if_valid(*args):
	if len(args) == 2:
		if CipherSolverIncludes.is_int(args[0]) and CipherSolverIncludes.is_int(args[1]):
			return False
		return True
	else:
		return True

def s_n_XOR(text, key):
	return "".join(chr(ord(i) ^ key) for i in text)

def s_s_XOR(t1, t2):
	assert len(t1) >= len(t2)
	pt = ""
	for i in range(len(t1)):
		pt += chr(ord(t1[i]) ^ ord(t2[i % len(t2)]))
	return pt

def decrypt(*args):
	#~ if len(args) == 2:
	args = list(args)
	if CipherSolverIncludes.is_int(args[0]) or CipherSolverIncludes.is_int(args[1]):
		if CipherSolverIncludes.is_int(args[0]):
			key = int(args[0])
			ct = int(args[1])
		else:
			key = int(args[1])
			ct = args[0]
		pt = s_n_XOR(ct, key)
		c, r, f = CipherSolverIncludes.readable_character_frequency(pt)
		return CipherSolverIncludes.return_value(pt, "numerical XOR", r)
	else:
		if len(args[0]) > len(args[1]):
			key = args[1]
			ct = args[0]
		elif len(args[1]) >= len(args[0]):
			key = args[0]
			ct = args[1]
		pt = s_s_XOR(ct, key)
		c, r, f = CipherSolverIncludes.readable_character_frequency(pt)
		return CipherSolverIncludes.return_value(pt, "string XOR", r)
	#~ else:
		#~ Ct = args[0]
		#~ possibles = [[s_n_XOR(Ct, key), key] for key in range(256)]
		#~ max_readable = [0, "", 0]
		#~ for t in possibles:
			#~ print t[1]
			#~ c = CipherSolverIncludes.count_words(t[0])
			#~ if c > max_readable[0]:
				#~ max_readable = [c, t[0], t[1]]
		#~ return CipherSolverIncludes.return_value(max_readable[1], "XOR with numerical key %d" % (max_readable[2]), max_readable[0])
#~ print decrypt(s_n_XOR("Hello World!{}", 64)).plaintext
#~ print repr(s_s_XOR("rasfsasrettlepinebec353luteayvlrghs3s", "easyctf"))
