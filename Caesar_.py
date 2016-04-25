import CipherSolverIncludes
import time

ARGS = [1, 2]

def is_int(string):
	for i in string:
		if i not in "0123456789":
			return False
	return True

def check_if_valid(*args):
	if len(args) == 2:
		integer  = [int(i) for i in args if is_int(i)]
		if len(integer) != 1:
			return False
		new_args = list(args)
		del new_args[args.index(str(integer[0]))]
	else:
		new_args = list(args)
	count = 0
	for i in new_args[0]:
		if i.lower() in "abcdefghijklmnopqrstuvwxyz":
			count += 1
	if float(count) / float(len(args[0])) > .5:
		return True
	return False

def shift(text, shift_val):
	final = ""
	for c in text:
		if c.lower() in "abcdefghijklmnopqrstuvwxyz":
			val = ord(c.lower()) - ord('a')
			val += shift_val
			val %= 26
			if c.lower() == c:
				final = final + chr(val + ord('a'))
			else:
				final = final + chr(val + ord('A'))
		else:
			final = final + c
	return final

def decrypt(*args):
	if len(args) == 2:
		integer  = [int(i) for i in args if is_int(i)]
		if len(integer) != 1:
			return False
		new_args = list(args)
		del new_args[args.index(str(integer[0]))]
		integer = integer[0]
		text = new_args[0]
		final = shift(text, integer)
		return CipherSolverIncludes.return_value(final, "Caesar cipher with key %s" % (integer), .9)
	else:
		text = args[0]
		plaintexts = [shift(text, i) for i in range(26)]
		m = [0, ""]
		t = time.time()
		times = []
		for p in plaintexts:
			count, r_frequency, f_table = CipherSolverIncludes.readable_character_frequency(p)
			spaces = f_table[" "] + f_table["_"]
			if spaces > .1:
				c = CipherSolverIncludes.count_words(p, True)
			c = CipherSolverIncludes.count_words(p)
			if m[0] < c:
				m = [c, p]
		count, r_frequency, f_table = CipherSolverIncludes.readable_character_frequency(p)
		spaces = f_table[" "] + f_table["_"]
		certainty = 0
		#~ if spaces > .01:
			#~ certainty = float(CipherSolverIncludes.count_words(m[1])) / float(len(m[1].replace("_", " ").split(" "))) #, True, True, CipherSolverIncludes.dictionary + CipherSolverIncludes.dict_oxford
		#~ else:
		certainty = r_frequency * .75
		if "flag" in m[1]:
			certainty = max([.9, certainty])
		return CipherSolverIncludes.return_value(m[1], "Caesar cipher with key %s" % (str(plaintexts.index(m[1]))), certainty)

if __name__ == "__main__":
	print shift("octopus pineapple priest pilot unique", 13)
	exit()
	print decrypt("'Idch' hr itrs 'Lnmj' hm QNS13, hrm's hs? Vzhs, mn, sgzs'r 'Yazw'. Zkrn, sgd ekzf hr itrs_z_vzqlto{hZpQduzT}").plaintext
	exit()
	print decrypt("shhg baa mbMemnppeyr e rhn .s tey'a ushcssnBpprii upeescweroceeaenrsis lad eeci pewdsonfoai rfonvltaeorsolon rc r, damew d na itdordtwloa.a iil r neot aeHklnhgc a,e rqed vusouv penowieErnlu rrlo eldeyimqs u ziusflmtasa olahbcrhr sieutecacntoe enughurh.dl sia iiblndMtnneyg ahe e ssre.tnb oti h oimir.earnen bn a.sl hdLr aetieudMn osftoagt ihrruoaane yi lrirw nelmt iWen seKlo ct; illhoh .n louet gbspn h. etet.e J o e .rdnor.r .aef e ,mc h.sS prei tiIeafs r dff Jo h.te.ofAa ,c h rvS t.ntteuAi hh n n.Leua Vg o r Ti Jcg DzneakeCrudvnenoe,iee,ena cr aamAayATln rt uwo StitsogDp oht ioeonieTcyef nnralc og,elehWf. a., a Pt. trtAri.Ah hlisV eCeedeoSfh xesltl.Ra tua inaoadg3gdnfiyi:hed r s tr GeiyWs Po,nea Hrv ygoaeeCSmifmjracan iunnasgWldmdrt otieileWmocnderaanetetyrn").plaintext
