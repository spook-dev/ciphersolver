from Tkinter import *
import CipherSolverIncludes
import time
import thread

#various cipher/encryption modules
import hex_
import base64_
import Caesar_
import morse_
import bacon_
import RSA_
import binary_
import XOR_
import trivial_

#enumeration of modules to be used later
#gets looped through and ciphers that we have
#valid ipts for get tried
modules = [hex_, base64_, Caesar_, morse_, bacon_, RSA_, binary_, XOR_, trivial_]

for module in modules:
	#but basically this bit makes sure that the required variables are present in
	#the module, and that they all are the required types
	vars_in_module = [item for item in dir(module) if not item.startswith("__")]
	ARGS_pass = True 
	check_if_valid_pass = True
	decrypt_pass = True
	if "ARGS" in vars_in_module:
		if type(module.ARGS) == type([]):
			for i in module.ARGS:
				if type(i) != type(0):
					ARGS_pass = False
		else:
			ARGS_pass = False
	else:
		ARGS_pass = False
	if not ARGS_pass:
		print "module %s does not have required variable ARGS defined properly" % (module.__name__)
		print "ARGS should be a list containing integers denoting the possible numbers of inputs to the decryption function"
	if "check_if_valid" in vars_in_module:
		if type(module.check_if_valid) != type(lambda: None):
			check_if_valid_pass = False
	else:
		check_if_valid_pass = False
	if not check_if_valid_pass:
		print "module %s does not have required variable check_if_valid defined properly" % (module.__name__)
		print "check_if_valid should be a function"


#dictionary is used to determine viability of plaintext
with open("dictionary.txt", "r") as dict_file:
	dictionary = dict_file.read().split("\n")

#simple output window. This is where viable plaintexts
#will be displayed
class OutputWindow(Tk):
	def __init__(self, message, title = "Output"):
		Tk.__init__(self, None)
		self.wm_title(title)
		self.opt = Text(self, width = 100, height = 40)
		self.opt.pack()
		self.opt.config(state = NORMAL)
		self.opt.insert(1.0, message)
		self.opt.config(state = DISABLED)
		self.mainloop()

"""
The main window. This is where all the magic happens.
All inputs are put here, and the algorithms that try all
decryption models and determine viability also happen here
"""
class InputWindow(Tk):
	def __init__(self, do_thread = True):
		Tk.__init__(self, None)
		self.wm_title("Cipher Solver")
		self.protocol("WM_DELETE_WINDOW", self.delete)

		#lists of dynamic input fields
		#used to organize field that are
		#constantly added or deleted
		self.ipts = []
		self.btns = []
		
		#self.commands is used to create static references from each
		#button to its row
		self.commands = []

		#add field button and "go" button have their own frame
		self.buttons_frame = Frame(self)
		self.buttons_frame.grid(row = 0, column = 0, columnspan = 2)
		self.add_field = Button(self.buttons_frame, text = "Add new field", command = self.create_row)
		self.add_field.grid(row = 0, column = 0)
		self.interpret_btn = Button(self.buttons_frame, text = "Go", command = self.interpret)
		self.interpret_btn.grid(row = 0, column = 1)

		#self.current_row is used to keep track of where to add rows
		self.current_row = 1
		#create the first row
		self.create_row()
		if do_thread:
			thread.start_new_thread(self.mainloop, ())
		else:
			self.mainloop()
	
	def delete(self):
		self.destroy()

	def create_row(self):
		#create a new entry field...
		self.ipts.append(Entry(self, width = 40))
		#temp variable is local, and so it creates an absolute reference to the row associated to
		#the button instead of a dynamic reference to self.current_row
		temp = self.current_row
		self.commands.append(lambda: self.delete_row(temp))
		#create a new row deletion button...
		self.btns.append(Button(self, text = "X", command = self.commands[temp - 1]))
		#grid 
		self.btns[-1].grid(row = self.current_row, column = 0)
		self.ipts[-1].grid(row = self.current_row, column = 1)
		self.current_row += 1

	def delete_row(self, row):
		#enumerate values to be replaced minues the deleted row's value
		values = [i.get() for i in self.ipts]
		#just delete the last row. This is so there's no mucking about with
		#trying to insert and delete things in the middle of other things
		self.ipts[-1].grid_remove()
		self.btns[-1].grid_remove()
		#delete the value that was on the row in question
		del values[row - 1]
		#delete the inputs and buttons that got un-gridded
		del self.ipts[-1]
		del self.btns[-1]
		self.current_row -= 1
		#replace values that didn't get deleted
		for i in range(len(self.ipts)):
			self.ipts[i].delete(0, END)
			self.ipts[i].insert(0, values[i])

	def interpret(self):
		global modules
		#get non empty values from input fields
		values = [i.get() for i in self.ipts if not len(i.get()) == 0]
		for n in range(len(values)):
			if values[n][:2] == "\\e":
				values[n] = eval('"' + values[n][2:] + '"')
		#all these modules are modules that accept this length of input
		#and the input is valid for that cipher/decryption
		valid_modules = [i for i in modules if len(values) in i.ARGS and i.check_if_valid(*values)]
		print "trying modules:"
		for m in valid_modules:
			print "	" + m.__name__
		viable_objects = [i.decrypt(*values) for i in valid_modules]
		viable_objects = [i for i in viable_objects if i.certainty > 0]
		viable_objects = sorted(viable_objects, key=lambda i: -i.certainty) #sorted defaults to ascending, the negative sign makes it descending
		printer = lambda i: "%s - %s: %s" % (i.certainty, i.description, i.plaintext.__repr__())
		OutputWindow("\n".join([printer(i) for i in viable_objects]))
		#OutputWindow("\n".join(plaintext_to_output))

if __name__ == "__main__":
	win = InputWindow(False)
