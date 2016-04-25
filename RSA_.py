import CipherSolverIncludes

ARGS = [4]

def to_text(num):
	s = hex(num).replace("0x", "").replace("L", "")
	if len(s) % 2 == 1:
		s = "0" + s
	return s.decode("hex")

def to_num(text):
	return eval("0x" + text.encode("hex"))

class RSA(object):
	def __init__(self, p = None, q = None, n = None, e = None, d = None, Pt = None, Ct = None, phi_n = None):
		self.p = p
		self.q = q
		self.n = n
		self.e = e
		self.d = d
		self.Pt = Pt
		self.Ct = Ct
		self.phi_n = phi_n
		self.calc_vars()
	
	def calc_vars(self):
		vars_exist = [self.calc_p(), self.calc_q(), self.calc_n(), self.calc_phi_n(), self.calc_e(), self.calc_d()]
		vars_prev = [False, False, False, False, False, False]
		count = 0
		while vars_exist != vars_prev and count <= 100:
			vars_prev = vars_exist
			vars_exist = [self.calc_p(), self.calc_q(), self.calc_n(), self.calc_phi_n(), self.calc_e(), self.calc_d()]
			count += 1
		if count == 100:
			print "maximum recursion exceeded. Probably an error in the program"
	
	def calc_p(self):
		if self.p == None:
			if self.q == None:
				if self.n == None:
					return False
				else:
					#we have to factor n
					pass
					return False
			else:
				self.p = self.n / self.q
		else:
			return True
	
	def calc_q(self):
		if self.q == None:
			if self.p == None:
				if self.n == None:
					return False
				else:
					#we have to factor n
					pass
					return False
			else:
				self.q = self.n / self.p
		else:
			return True
	
	def calc_n(self):
		#so we need n, or p&q
		if self.n == None:
			if self.p == None or self.q == None:
				return False
			else:
				self.n = self.p*self.q
		else:
			return True
	
	def calc_phi_n(self):
		if self.phi_n == None:
			if self.p != None and self.q != None:
				self.phi_n = (self.p - 1) * (self.q - 1)
			#else we're gonna have to factor n in which case FUUUUUUUCK
			else:
				return False
		else:
			return True
	
	def calc_e(self):
		if self.e == None:
			if self.d == None:
				self.e = 65537 #could also try 3
			else:
				if self.calc_n() != False:
					self.e = inv(self.d, self.phi_n)
				else:
					return False
		else:
			return True
	
	def calc_d(self):
		if self.d == None:
			if self.calc_phi_n() != False:
				self.d = inv(self.e, self.phi_n)
			else:
				return False
		else:
			return True
	
	def encrypt(self, Pt = None):
		if type(Pt) == type(""):
			Pt = to_num(Pt)
		if Pt != None:
			self.Pt = Pt
		if self.Pt != None and self.e != None and self.n != None:
			self.Ct = pow(self.Pt, self.e, self.n)
			return self.Ct
		else:
			print "Not enough variables defined for encryption"
			return False
	
	def decrypt(self, Ct = None):
		if Ct != None:
			self.Ct = Ct
		if self.Ct != None and self.d != None and self.n != None:
			self.Pt = pow(self.Ct, self.d, self.n)
			return self.Pt
		else:
			print "Not enough variables defined for decryption"
			return False
	def print_vars(self):
		print "p = %s" % (self.p)
		print "q = %s" % (self.q)
		print "n = %s" % (self.n)
		print "e = %s" % (self.e)
		print "d = %s" % (self.d)
		print "Pt = %s" % (self.Pt)
		print "Ct = %s" % (self.Ct)
		print "Phi(n) = %s" % (self.phi_n)
	
def gcd(a,b):
  """Returns the gcd of its inputs times the sign of b if b is nonzero,
  and times the sign of a if b is 0.
  """
  while b != 0:
	  a,b = b, a % b
  return a


def inv(p, q):
	"""Multiplicative inverse"""
	def xgcd(x, y):
		"""Extended Euclidean Algorithm"""
		s1, s0 = 0, 1
		t1, t0 = 1, 0
		while y:
			q = x // y
			x, y = y, x % y
			s1, s0 = s0 - q * s1, s1
			t1, t0 = t0 - q * t1, t1
		return x, s0, t0	  
 
	s, t = xgcd(p, q)[0:2]
	assert s == 1
	if t < 0:
		t += q
	return t

def check_if_valid(*args):
	args = list(args)
	for i in args:
		if not CipherSolverIncludes.is_int(i):
			return False
	args = [eval(i) for i in list(args)]
	RSA(p = args[0], q = args[1], e = args[2], Ct = args[3])
	try:
		RSA(p = args[0], q = args[1], e = args[2], Ct = args[3])
		return True
	except:
		return False

def decrypt(*args):
	args = [eval(i) for i in list(args)]
	r = RSA(p = args[0], q = args[1], e = args[2], Ct = args[3])
	return CipherSolverIncludes.return_value("%s ---- %s" % (r.decrypt(), to_text(r.decrypt())), "RSA", 1.0)



if __name__ == "__main__":
	e = 340035333160956238336074318075946961695270890880263371398510321485728225
	m = 614010459838253953596498114943057697842675637887066261109163514805589167
	c = 416808431213057812839807235099929401146034654633863359116938353620975451
	p = 783420406144696097385833069281677113
	q = 783756020423148789078921701951691559
	d = 65537
	r = RSA(e = e, n = m, Ct = c, p = p, q = q, d = d)
	print to_text(r.decrypt())
	exit()
	
	p = 2425967623052370772757633156976982469681
	q = 1451730470513778492236629598992166035067
	e = 65537
	n = p*q
	phin = (p-1)*(q-1)
	d = inv(e, phin)
	r = RSA(n = n, p = p, d = d)
	
	print len(hex(r.n).replace("0x", "").replace("L", "")) /2
	print len("This is a string that contains t")
	print "This is a string that contains t".encode("hex")
	r.encrypt("This is a string that contains t")
	print to_text(r.decrypt())
	Pt = eval("0x" + "Hello World!".encode("hex"))
	Ct = pow(Pt, e, n)
	Pt = pow(Ct, d, n)
	#print to_text(Pt)
