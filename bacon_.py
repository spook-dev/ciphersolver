import CipherSolverIncludes

ARGS = [1]

def check_if_valid(in_val):
	if type(in_val) != type(''):
		return False
	if len(in_val.replace(" ", "")) % 5 != 0:
		return False
	for i in in_val.lower():
		if i != 'a' and i != 'b' and i != ' ':
			return False
	return True

def decrypt(in_val):
	count=0
	possible_sol = ''
	bacon = {'AAAAA':'a','AABBA':'g','ABBAA':'n','BAABA':'t', 
'AAAAB':'b','AABBB':'h','ABBAB':'o','BAABB':'u',	 
'AAABA':'c','ABAAA':'i','ABBBA':'p','BABAA':'w',	 
'AAABB':'d','ABAAB':'k','ABBBB':'q','BABAB':'x',	 
'AABAA':'e','ABABA':'l','BAAAA':'r','BABBA':'y',	 
'AABAB':'f','ABABB':'m','BAAAB':'s','BABBB':'z',	 
'ABAAA':'j','BAABB':'v',}
	five_character_clump = ''
	for i in in_val:
		count += 1
		if len(five_character_clump) == 5:
			for a in bacon.keys():
				if a == five_character_clump:
					possible_sol += str(bacon[a])
					if i == ' ':
						possible_sol += ' '	
						five_character_clump = ''
					elif i != ' ':
						five_character_clump = i
		elif len(five_character_clump) < 5:
			five_character_clump += str(i)
			if count == len(in_val):
				possible_sol += bacon[five_character_clump]
	return CipherSolverIncludes.return_value(possible_sol, "Bacon cipher", 1.0)
