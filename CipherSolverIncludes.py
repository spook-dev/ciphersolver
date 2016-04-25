class return_value(object):
	def __init__(self, plaintext, description, certainty):
		self.plaintext = plaintext
		self.description = description
		self.certainty = certainty
with open("dictionary.txt", "r") as dict_file:
	dictionary = dict_file.read().split("\n")
with open("dict_oxford.txt", "r") as dict_file:
	dict_oxford = [i.lower() for i in dict_file.read().split("\n")]

#various generic viability algorithms
dict_oxford_abridged = [i for i in dict_oxford if len(i) > 3]
def count_words(text, separated = False, dict_in_use = dict_oxford_abridged):
	count = 0
	if separated:
		text = [i.lower() for i in text.replace("_", " ").split(" ")]
		for i in text:
			if i.lower() in dict_in_use:
				count += 1
		return count
	for i in dict_in_use:
			count += text.lower().count(i)
	return count

#~ print count_words("Genius without education is like silver in the mine", True, True, dictionary + dict_oxford)

def readable_character_frequency(text):
	text = text.lower()
	readable = "1234567890-=;',./\\!@#$%^&*_+:\"? abcdefghijklmnopqrstuvwxyz{}"
	f = {}
	for i in readable:
		f[i] = 0
	count = 0
	for i in text:
		if i in readable:
			count += 1
			f[i] += 1
	for key in f.keys():
		if count != 0:
			f[key] = float(f[key]) / float(count)
		else:
			f[key] = 0.0
	if len(text) != 0:
		return count, float(count)/float(len(text)), f
	else:
		return count, 0, f

def count_space_characters(text):
	count = 0
	for i in text:
		if i in " _":
			count += 1
	return count

def is_flag_format(text):
	if text[:5] == "flag{" and text[-1] == "}":
		return True
	return False

def is_int(text):
	for i in text:
		if i not in "0123456789":
			return False
	return True
